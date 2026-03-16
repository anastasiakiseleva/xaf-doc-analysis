---
uid: DevExpress.ExpressApp.Core.IObjectSpaceProviderFactory
name: IObjectSpaceProviderFactory
type: Interface
summary: A service that provides access to Object Space Providers registered in your ASP.NET Core application.
syntax:
  content: public interface IObjectSpaceProviderFactory
seealso:
- linkId: DevExpress.ExpressApp.Core.IObjectSpaceProviderFactory._members
  altText: IObjectSpaceProviderFactory Members
- linkId: DevExpress.ExpressApp.XafApplication.CreateObjectSpace*
- linkId: DevExpress.ExpressApp.XafApplication.ObjectSpaceProviders*
- linkId: DevExpress.ExpressApp.IObjectSpaceFactory
- linkId: DevExpress.ExpressApp.INonSecuredObjectSpaceFactory
---
In ASP.NET Core Blazor and Web API applications, @DevExpress.ExpressApp.IObjectSpaceFactory services use `IObjectSpaceProviderFactory` to create the collection of @DevExpress.ExpressApp.IObjectSpaceProvider objects. 

Refer to the following topic to learn how to add your custom object space provider to the application: [Configure Your Application to Use Custom Object Space Provider](xref:405388#3-configure-your-application-to-use-custom-object-space-provider). 