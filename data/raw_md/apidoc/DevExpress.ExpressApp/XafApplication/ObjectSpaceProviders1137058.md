---
uid: DevExpress.ExpressApp.XafApplication.ObjectSpaceProviders
name: ObjectSpaceProviders
type: Property
summary: Gets a list of Object Space Providers used by [](xref:DevExpress.ExpressApp.XafApplication).
syntax:
  content: |-
    [Browsable(false)]
    public IList<IObjectSpaceProvider> ObjectSpaceProviders { get; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{DevExpress.ExpressApp.IObjectSpaceProvider}
    description: An **IList\<**[](xref:DevExpress.ExpressApp.IObjectSpaceProvider)**>** list of Object Space Providers.
seealso: []
---
XAF uses an Object Space Provider to create [Object Spaces](xref:113707). The following Object Space Provider types are supplied with XAF:

Space Provider | Object Space
---------|----------
@DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider | @DevExpress.ExpressApp.Xpo.XPObjectSpace
@DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1 | @DevExpress.ExpressApp.EFCore.EFCoreObjectSpace
@DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider | @DevExpress.ExpressApp.Security.SecuredXPObjectSpace
@DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 | @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpace
@DevExpress.ExpressApp.NonPersistentObjectSpaceProvider | @DevExpress.ExpressApp.NonPersistentObjectSpace

XAF applications configure Object Space Providers through the Application Builder's @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder.ObjectSpaceProviders property. When you use the [Template Kit](xref:405447) to create an application, it adds the Object Space Providers to your application based on the specified presets. 

Refer to the following topic to learn how to add custom Object Space Providers to your application: <xref:405388>.

[!include[MultipleOSProvidersNote](~/templates/multipleosprovidersnote11196.md)]