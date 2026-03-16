---
uid: DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs.ObjectSpaceProviders
name: ObjectSpaceProviders
type: Property
summary: Specifies a custom list of Object Space Providers to be used by the application.
syntax:
  content: public List<IObjectSpaceProvider> ObjectSpaceProviders { get; }
  parameters: []
  return:
    type: System.Collections.Generic.List{DevExpress.ExpressApp.IObjectSpaceProvider}
    description: An **IList\<**[](xref:DevExpress.ExpressApp.IObjectSpaceProvider)**>** list of custom Object Space Providers to be used by the application.
seealso: []
---
When several Object Space Providers are passed to the **ObjectSpaceProviders** property, the Object Space Provider appropriate for each particular business object type is determined automatically. However, if you want to create an Object Space manually, use an overload of the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method that takes the _objectType_ parameter.

The passed list is assigned to the [XafApplication.ObjectSpaceProviders](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceProviders) property.

[!include[MultipleOSProvidersNote](~/templates/multipleosprovidersnote11196.md)]

[!include[Object Space Providers Order](~/templates/objectspaceprovidersorder.md)]