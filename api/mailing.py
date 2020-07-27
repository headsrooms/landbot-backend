import logging
import smtplib
import ssl
from asyncio import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from api import settings


def render_template(username, email) -> str:
    template = f"""
      <div style="background-color:#f1f3f9">

                  <table role="presentation" style="height:33px;background:#f1f3f9;font-size:0px;width:100%" cellspacing="0" cellpadding="0" border="0">
                     <tbody>
                        <tr>
                           <td>
                              <div style="margin:0px auto;max-width:600px">
                                 <table role="presentation" style="font-size:0px;width:100%" cellspacing="0" cellpadding="0" border="0" align="center">
                                    <tbody>
                                       <tr>
                                          <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:0px 0px 0px 0px">

                                                      <div class="m_-6024400879050985559mj-column-per-100" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%">
                                                         <table role="presentation" style="vertical-align:top" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                            <tbody></tbody>
                                                         </table>
                                                      </div>

                                          </td>
                                       </tr>
                                    </tbody>
                                 </table>
                              </div>
                           </td>
                        </tr>
                     </tbody>
                  </table>

                  <div style="margin:0px auto;max-width:600px;background:#ffffff;border:1px solid #d2d5e2">
                     <table role="presentation" style="font-size:0px;width:100%;background:#ffffff" cellspacing="0" cellpadding="0" border="0" align="center">
                        <tbody>
                           <tr>
                              <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:0px 0px 0px 0px">

                                          <div class="m_-6024400879050985559mj-column-per-100" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%">
                                             <table role="presentation" style="vertical-align:top;margin-top:36px" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                <tbody>
                                                   <tr>
                                                      <td style="word-wrap:break-word;font-size:0px;padding:0px 68px 36px 67px" align="left">
                                                         <div id="m_-6024400879050985559emailContent" style="color:#4c4f6d;font-family:Helvetica,sans-serif;font-size:15px;line-height:1.5;text-align:left">
                                                            <p>Welcome, {username}<br> Your account has been created! <br> Email: {email}</p>
                                                         </div>
                                                      </td>
                                                   </tr>
                                                </tbody>
                                             </table>
                                          </div>

                              </td>
                           </tr>
                        </tbody>
                     </table>
                  </div>


                  <div id="m_-6024400879050985559powered" style="border:1px solid #d2d5e2;border-top:none;margin:0px auto;max-width:600px;background:#f9fafc">
                     <table role="presentation" style="font-size:0px;width:100%;background:#f9fafc" cellspacing="0" cellpadding="0" border="0" align="center">
                        <tbody>
                           <tr>
                              <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:0">

                                          <div class="m_-6024400879050985559mj-column-per-100" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%">
                                             <table role="presentation" style="vertical-align:top" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                <tbody>
                                                   <tr>
                                                      <td style="word-wrap:break-word;font-size:0px;padding:15px 15px 15px 15px" align="center">
                                                         <div style="color:#4c4f6d;font-family:Ubuntu,Helvetica,Arial,sans-serif;font-size:11px;line-height:1.5;text-align:center">
                                                            <p id="m_-6024400879050985559poweredContent" style="font-family:Helvetica,sans-serif;font-size:15px;color:#4c4f6d;margin:3px 0 5px"><span style="font-size:12px">
                                                              <span style="color:#91a1b5">We're ⚡️ by </span> <a href="https://landbot.io" style="color:#72859e" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://landbot.io&amp;source=gmail&amp;ust=1595931140214000&amp;usg=AFQjCNEgScnS_PUez7lcFjch77lMBLNp5g"><span style="color:#72859e"><strong>Landbot.io</strong></span></a></span>
                                                            </p>
                                                         </div>
                                                      </td>
                                                   </tr>
                                                </tbody>
                                             </table>
                                          </div>

                              </td>
                           </tr>
                        </tbody>
                     </table><div class="yj6qo"></div><div class="adL">
                  </div></div><div class="adL">




      </div></div><div class="adL">
   </div>"""

    return template


def create_message(username, sender_email: str, receiver_email: str) -> MIMEMultipart:
    message = MIMEMultipart("alternative")
    message["Subject"] = f"Welcome, {username}"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    # text = """\
    # Hi,
    # How are you?
    # Real Python has many great tutorials:
    # www.realpython.com"""
    html = render_template(username, receiver_email)

    # Turn these into plain/html MIMEText objects
    # part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    # message.attach(part1)
    message.attach(part2)

    return message


async def send_welcome_email(to_address: str, username: str, bypass: bool):
    if bypass:
        logging.info("Bypassed mail sending")
        return
    await sleep(settings.SLEEP_TIME_IN_SECONDS_BEFORE_SEND_EMAIL)
    port = settings.SSL_PORT
    password = settings.SMTP_PASSWORD
    sender_email = settings.SENDER_EMAIL

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        message = create_message(username, sender_email, to_address)
        server.sendmail(sender_email, to_address, message.as_string())
