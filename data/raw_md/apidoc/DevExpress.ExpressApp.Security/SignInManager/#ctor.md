---
uid: DevExpress.ExpressApp.Security.SignInManager.#ctor(DevExpress.ExpressApp.Security.ISecurityStrategyBase,DevExpress.ExpressApp.INonSecuredObjectSpaceFactory,DevExpress.ExpressApp.Security.Authentication.Internal.IStandardAuthenticationIdentityCreator,System.IServiceProvider,DevExpress.ExpressApp.Security.IPrincipalProvider)
name: SignInManager(ISecurityStrategyBase, INonSecuredObjectSpaceFactory, IStandardAuthenticationIdentityCreator, IServiceProvider, IPrincipalProvider)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.Security.SignInManager class with specified settings. You do not need to call this constructor, it is called internally by the DI container.
syntax:
  content: public SignInManager(ISecurityStrategyBase security, INonSecuredObjectSpaceFactory objectSpaceFactory, IStandardAuthenticationIdentityCreator identityCreator, IServiceProvider serviceProvider, IPrincipalProvider principalProvider)
  parameters:
  - id: security
    type: DevExpress.ExpressApp.Security.ISecurityStrategyBase
    description: A class that implements the @DevExpress.ExpressApp.Security.ISecurityStrategyBase interface.
  - id: objectSpaceFactory
    type: DevExpress.ExpressApp.INonSecuredObjectSpaceFactory
    description: A class that implements the DevExpress.ExpressApp.Core.INonSecuredObjectSpaceFactory interface.
  - id: identityCreator
    type: DevExpress.ExpressApp.Security.Authentication.Internal.IStandardAuthenticationIdentityCreator
    description: A class that implements the `IStandardAuthenticationIdentityCreator` interface.
  - id: serviceProvider
    type: System.IServiceProvider
    description: A class that implements the @System.IServiceProvider interface.
  - id: principalProvider
    type: DevExpress.ExpressApp.Security.IPrincipalProvider
    description: A class that implements the `DevExpress.ExpressApp.Security.IPrincipalProvider` interface.
seealso: []
---
