'use strict';
let nodemailer = require('nodemailer');
let smtpTransport = require('nodemailer-smtp-transport');
let config = require('./config.js');
//parses the email string
let getEmail = function(st) {
    if (st.indexOf('mailto:') === -1) {
        //not found
        return st;
    } else {
        let tmp = st.split('mailto:');
        return tmp[1];
    }
}
module.exports = {
    sendMail: function(type, from, to, subject, text, html) {
        switch (type) {
            case 'userActivation':
                subject = config.emailTemplates.userActivation.subject;
                text = config.emailTemplates.userActivation.text;
                if (!from) {
                    from = config.sender;
                }
                break;
            case 'userRegistration':
                subject = config.emailTemplates.userRegistration.subject;
                text = config.emailTemplates.userRegistration.text;
                if (!to) {
                    to = config.sender;
                }
                break;
            default:
                subject = subject;
                text = text;
                if (!from) {
                    from = config.sender;
                }
        }
        let transporter = nodemailer.createTransport(smtpTransport(config.emailConfig));
        // send mail
        transporter.sendMail({
            from: getEmail(from),
            to: getEmail(to),
            subject: subject,
            text: text
        }, function(error, info) {
            if (error) {
                console.log(error);
            } else {
                console.log('Message sent: ' + info.response);
            }
        });
    }
}
