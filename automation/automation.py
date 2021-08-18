import re


def reading_file(path:str):
    with open(path,'r')as opened:
        reading=opened.read().strip()
        return reading




def add_emails(reading):
    pettern = r'([\w\.-]+)@([\w\.-]+)'
    emails=re.findall(pettern,reading)
    num=len(emails)
    for x in range(num):
        temp =emails[x]
        emails[x]='@'.join(temp)
    emails.sort()
    emails=list(set(emails))
    final_text=''
    for x in emails:
        final_text+=x
        final_text+='\n'
    
    # print(final_text)
    with open('assets/emails.txt','w') as final_file:
        final_file.write(f'{final_text}')    


def add_phones(reading):
    pettern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    phones=re.findall(pettern,reading)
    # for i in range(len(phones)):
    #     phones[i]= list(phones[i])
    #     phones[i][4]=''
    #     phones[i][6]=''
    #     phones[i]= ''.join(phones[i])
    # print(phones)

    phones=list(set(phones))
    edit_phones=[]
    for i in phones:
        if i[0]=='(':
            i=str(i[1:])
            i= str(i[0:3])+'-'+str(i[4:7])+'-'+str(i[8:])
        if i[3]=='.':
            i= str(i[0:3])+'-'+str(i[4:7])+'-'+str(i[8:])
        if i[3]!='-':
            i= str(i[0:3])+'-'+str(i[3:6])+'-'+str(i[6:]) 
        i='206-'+str(i)
        
        edit_phones.append(i)
    edit_phones.sort()
    # print(edit_phones)
    final_text=''
    for x in edit_phones:
        final_text+=x
        final_text+='\n'
    with open('assets/phone_numbers.txt','w') as final_file:
        final_file.write(f'{final_text}')












if __name__=='__main__':
    add_emails(reading_file('assets/potential-contacts.txt'))
    add_phones(reading_file('assets/potential-contacts.txt'))