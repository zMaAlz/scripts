#Забирает пользователей и атрибуты из группы в AD
$Groupe_AD = 'Exemple'
$Path_save = 'c:\temp\AD_users.csv'
Import-Module activedirectory
Get-ADGroupMember -Identity $Groupe_AD -recursive | foreach { Get-ADUser $_ -properties MobilePhone, telephoneNumber, SamAccountName, DisplayName, DistinguishedName, Description, Title } | Export-csv -path $Path_save -Append -NoTypeInformation