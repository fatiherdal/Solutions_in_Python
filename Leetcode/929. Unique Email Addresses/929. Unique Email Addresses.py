        def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
            def control (mail):
                first_sep = mail.index('@')
                first_local = mail[:first_sep-1]
                domain = mail[first_sep:]
                if '+' in first_local:
                    second_sep = first_local.index('+')
                    second_local = first_local[:second_sep]
                else:
                    second_local = first_local
                n = 0
                while n == 0:
                    if '.' in second_local:
                        second_local = second_local.replace('.', '')
                    else:
                        break
                return second_local+domain

            new_mails = []
            for mail in emails:
                new_mails.append(control(mail))

            return len(set(new_mails))