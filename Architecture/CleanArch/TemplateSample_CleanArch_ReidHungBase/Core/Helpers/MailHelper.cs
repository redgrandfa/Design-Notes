using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Mail;
using System.Text;

namespace Common.Helpers
{
    internal class MailHelper
    {
        internal static void SendMail(List<string> recipientList, string subject, string body)
        {
            string SenderAccount = "reidtest12@gmail.com";
            string Password = "dr0wss@P";

            // 設定兩大區塊 服務 郵件，順序無所謂
            #region 服務
            SmtpClient client = new SmtpClient();
            client.Host = "smtp.gmail.com";
            client.Port = 587; //通訊埠
            // smtp通常是587 ，
            // sqlserver 通常是1433 (通常不會亂改)
            // 80: 通常http
            // 443: https

            // 也可以利用建構式多載 
            //SmtpClient client2 = new SmtpClient("smtp.gmail.com", 587);

            //憑證
            client.Credentials = new NetworkCredential(SenderAccount, Password);
            client.EnableSsl = true;
            #endregion

            #region 郵件
            MailMessage mail = new MailMessage();
            mail.From = new MailAddress(SenderAccount, "筆試習題服務");  //寄件人
            recipientList.ForEach(addr => mail.To.Add(addr));  //收件人

            //mail.Priority = MailPriority.High;

            //主旨
            mail.Subject = subject;
            mail.SubjectEncoding = Encoding.UTF8; //應該是有中文 就需要

            //內文
            mail.Body = body;
            //mail.BodyEncoding = Encoding.UTF8; //應該是有中文 就需要
            mail.IsBodyHtml = true;

            //附件
            //Attachment attachment = new Attachment( @"C:\fakepath\fake.txt" );  
            //@ 是 【逐字字串常值】， 會使得反斜線 無效果
            //mail.Attachments.Add(attachment);

            #endregion

            try
            {
                client.Send(mail); //Send 是內建的方法
            }
            catch (Exception ex)
            {
                throw ex;
                //無法寄信的處理
                //https://blog.no2don.com/2021/01/c-gmail-smtp-server-requires-secure.html
                //1. 低安全性應用程式  開啟 (已設兩步驟驗證 的帳號無法設定)
                //2. 啟用 IMAP
            }
            finally
            {
                //attachment.Dispose();
                mail.Dispose();
                client.Dispose();
            }
        }
    }
}
