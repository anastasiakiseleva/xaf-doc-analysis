---
uid: DevExpress.ExpressApp.Security.SecurityOptions.RefreshTokenExpiration
name: RefreshTokenExpiration
type: Property
summary: Specifies how long the refreshed token is valid. The refresh token lets you get new JWT access tokens after old tokens expire.
syntax:
  content: public TimeSpan RefreshTokenExpiration { get; set; }
  parameters: []
  return:
    type: System.TimeSpan
    description: Refreshed token lifetime.
seealso: []
defaultMemberValue: TimeSpan.FromMinutes(30)
---