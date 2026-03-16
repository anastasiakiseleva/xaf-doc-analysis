---
uid: DevExpress.ExpressApp.Security.UserManager.#ctor(System.IServiceProvider,DevExpress.ExpressApp.Security.IPrincipalProvider,DevExpress.ExpressApp.Security.IUserLockout,Microsoft.Extensions.Options.IOptions{DevExpress.ExpressApp.Security.SecurityOptions})
name: UserManager(IServiceProvider, IPrincipalProvider, IUserLockout, IOptions<SecurityOptions>)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.Security.UserManager class with specified settings. You do not need to call this constructor; it is called internally by the DI container.
syntax:
  content: public UserManager(IServiceProvider serviceProvider, IPrincipalProvider principalProvider, IUserLockout userLockout, IOptions<SecurityOptions> securityOptions)
  parameters:
  - id: serviceProvider
    type: System.IServiceProvider
    description: A class that implements the @System.IServiceProvider interface.
  - id: principalProvider
    type: DevExpress.ExpressApp.Security.IPrincipalProvider
    description: A class that implements the `DevExpress.ExpressApp.Security.IPrincipalProvider` interface.
  - id: userLockout
    type: DevExpress.ExpressApp.Security.IUserLockout
    description: A class that implements the `DevExpress.ExpressApp.Security.IUserLockout` interface.
  - id: securityOptions
    type: Microsoft.Extensions.Options.IOptions{DevExpress.ExpressApp.Security.SecurityOptions}
    description: A @DevExpress.ExpressApp.Security.SecurityOptions object wrapped into [IOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.ioptions-1).
seealso: []
---
