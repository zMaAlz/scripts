# Выгружаем список групп и пользователей групп из AD
# Группы распространения должны находиться в "OU=MailDistribution"
# Перез запуском необходимо удалить файлы из  $Path_save_dir и удалить файл $Path_save

$Path_save = 'c:\temp\AD_group_for_yandex.csv'
$Path_save_dir = 'C:\temp\ad_groups\'

Import-Module activedirectory

# Выбираем группы из AD и записываем в CSV по адресу $Path_save
Write-Host "Import Distribution Group"
Get-ADGroup -Filter {GroupCategory -eq "Distribution"} -SearchBase "OU=MailDistribution,DC=exemple,DC=local" | Select-Object -Property SamAccountName | Export-csv -path $Path_save -Append -NoTypeInformation
Write-Host "Import Complite"
# Загружаем CSV и выбираем пользователей группы ( сохраняем в $Path_save_dir)
$group_import = Import-Csv -Path $Path_save

ForEach ($item in $group_import){
   $groupe_name = $item.SamAccountName
   $Path_save_group_users = $Path_save_dir + $groupe_name + '.csv'
   Write-Host "Users from  $groupe_name import to $Path_save_group_users"
   Get-ADGroupMember -Identity $groupe_name -recursive | ForEach-Object { Get-ADUser $_ -properties SamAccountName, DisplayName, Description } | Export-csv -path $Path_save_group_users -Append -NoTypeInformation
}