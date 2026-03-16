---
uid: DevExpress.ExpressApp.Security.UserManager.CreateUser``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.String,System.Action{``0})
name: CreateUser<TUser>(IObjectSpace, String, String, Action<TUser>)
type: Method
summary: Creates a new user with the specified settings.
syntax:
  content: |-
    public UserResult<TUser> CreateUser<TUser>(IObjectSpace objectSpace, string userName, string password, Action<TUser> customizeUser = null)
        where TUser : class, ISecurityUserWithLoginInfo, IAuthenticationStandardUser
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An Object Space used to create the user.
  - id: userName
    type: System.String
    description: A user name for the new user.
  - id: password
    type: System.String
    description: A password for the new user.
  - id: customizeUser
    type: System.Action{{TUser}}
    defaultValue: "null"
    description: A delegate method used to additionally customize the created user object.
  typeParameters:
  - id: TUser
    description: A user object type.
  return:
    type: DevExpress.ExpressApp.Security.UserResult{{TUser}}
    description: An object that contains the result of the user creation operation.
seealso: []
---

Use this method to create and customize a new application user as the following code snippet demonstrates:

[!include[usermanager-create-user-example](~/templates/usermanager-create-user-example.md)]

[!include[usermanager-user-result](~/templates/usermanager-user-result.md)]