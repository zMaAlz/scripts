Set myOlApp = CreateObject("Outlook.Application") 
Set olMAPI = myOlApp.GetNameSpace("MAPI") 
Set olInbox = olMAPI.GetDefaultFolder(6)
Set eMaills = olInbox.Items

'olInbox.Items.Restrict("[Unread]=true")
'Set oneEm = eMaills(MailItem)
'Set oCollMail = eMaills.GetTable
'Set fSf = C:\temp\
'Set newEmail = oCollMail.MailItem
'Set oAtt = newEmail.Attachment

'oneEm.SaveAsFile fSf & oneEm.FileName

'If eMaills = MailItem Then 	
For Each MailItem In eMaills
	'For Each oneEm.Attachments In eMaills
	MailItem.SaveAsFile C:\temp\ & MailItem.FileName
	'Next
Next
'end if
