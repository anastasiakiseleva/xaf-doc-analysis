---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UsePasswordAuthentication(System.Action{DevExpress.ExpressApp.Security.IAuthenticationStandardLogonParameters})
name: UsePasswordAuthentication(Action<IAuthenticationStandardLogonParameters>)
type: Method
summary: Configures the client to use authentication with login and password specified in a delegate.
syntax:
  content: public MiddleTierClientBuilder<TDbContext> UsePasswordAuthentication(Action<IAuthenticationStandardLogonParameters> populateLogonParameters)
  parameters:
  - id: populateLogonParameters
    type: System.Action{DevExpress.ExpressApp.Security.IAuthenticationStandardLogonParameters}
    description: A delegate invoked to obtain client authentication credentials. It should write the login and password to the delegate parameter that implements the `IAuthenticationStandardLogonParameters` interface.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder{{TDbContext}}
    description: The builder that allows you to further configure the Middle Tier client.
seealso:
- linkId: "404389"
- linkId: "404398"
---
