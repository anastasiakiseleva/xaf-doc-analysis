---
uid: DevExpress.ExpressApp.Security.SecurityOptions.AccessTokenExpiration
name: AccessTokenExpiration
type: Property
summary: Specifies the lifetime of the JWT access token. The token authenticates requests between the client application and the Middle Tier server.
syntax:
  content: public TimeSpan AccessTokenExpiration { get; set; }
  parameters: []
  return:
    type: System.TimeSpan
    description: The JWT access token lifetime.
seealso: []
defaultMemberValue: TimeSpan.FromMinutes(15)
---