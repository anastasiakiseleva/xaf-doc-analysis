---
uid: DevExpress.ExpressApp.XafApplication.ObjectSpaceProvider
name: ObjectSpaceProvider
type: Property
summary: Provides access to the application's Object Space Provider.
syntax:
  content: |-
    [Browsable(false)]
    public IObjectSpaceProvider ObjectSpaceProvider { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.IObjectSpaceProvider
    description: An instance of the class that implements the [](xref:DevExpress.ExpressApp.IObjectSpaceProvider) interface.
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.CreateObjectSpace*
---
XAF uses an Object Space Provider to create [Object Spaces](xref:113707). XAF applications configure Object Space Providers through the Application Builder's @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder.ObjectSpaceProviders property. When you use the [Template Kit](xref:405447) to create an application, it adds the Object Space Providers to your application based on the specified presets. 

> [!NOTE]
> [!include[Object Space Providers Order](~/templates/objectspaceprovidersorder.md)]