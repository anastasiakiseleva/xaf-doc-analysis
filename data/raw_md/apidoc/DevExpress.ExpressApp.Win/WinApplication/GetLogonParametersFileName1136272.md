---
uid: DevExpress.ExpressApp.Win.WinApplication.GetLogonParametersFileName(System.String)
name: GetLogonParametersFileName(String)
type: Method
summary: Returns a name for the file where logon parameters are stored.
syntax:
  content: |-
    [Browsable(false)]
    public static string GetLogonParametersFileName(string path)
  parameters:
  - id: path
    type: System.String
    description: A string that is the path to the file where logon parameters must be stored.
  return:
    type: System.String
    description: A string that is the name of the file where logon parameters are stored.
seealso: []
---
To show the logon parameters of the last user who logged on, they are saved to a file. To get the name of this file, the **GetLogonParametersFileName** method is used. This method combines the path passed as the _path_ parameter with the **LogonParameters** string. By default, the path for this file is the same as the path of the Model.User.xafml file.