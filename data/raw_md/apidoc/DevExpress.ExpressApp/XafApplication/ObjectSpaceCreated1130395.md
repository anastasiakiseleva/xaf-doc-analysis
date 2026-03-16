---
uid: DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated
name: ObjectSpaceCreated
type: Event
summary: Occurs after an [Object Space](xref:113707) has been created via the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method.
syntax:
  content: public event EventHandler<ObjectSpaceCreatedEventArgs> ObjectSpaceCreated
seealso: []
---

> [!NOTE]
> This is a legacy event. In new applications, we recommend that you use the [ObjectSpaceProviderEvents.OnObjectSpaceCreated ](xref:DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated) event for most use case scenarios. Refer to the [Usage Considerations](#usage-considerations) section for details.

If you need to access the Object Space created for a particular View, handle the **ObjectSpaceCreated** event and use its **ObjectSpaceCreatedEventArgs.ObjectSpace** parameter.

Note that nested Object Spaces are created by the [XPObjectSpace.CreateNestedObjectSpace](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateNestedObjectSpace) method. So, the `ObjectSpaceCreated` event is not raised when a nested Object Space is created.

## Usage Considerations

The `XafApplication.ObjectSpaceCreated` event fires only for Object Spaces that are created by an XAF Application and within the XAF Application context (for example, in an [XAF Controller](xref:112621)).

Keep in mind that `XafApplication` does not host the Object Space creation logic and instead uses the @DevExpress.ExpressApp.IObjectSpaceFactory service to create Object Spaces. Other services can also directly use `IObjectSpaceFactory` to create Object Spaces without communicating with `XafApplication`. In such cases, the [`ObjectSpaceProviderEvents.OnObjectSpaceCreated`](xref:DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated) event fires when an Object Space is created, but the `XafApplication.ObjectSpaceCreated` event does not. 

Adhere to the following recommendations to choose the correct event to use:

- If you need to implement global logic that must be triggered by the creation of any `IObjectSpace` within the application, use [`ObjectSpaceProviderEvents.OnObjectSpaceCreated`](xref:DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated).
- If logic that you want to implement operates on XAF Application elements (XAF Controllers, View UI elements, and so on), you may prefer to use `XafApplication.ObjectSpaceCreated` for convenience.
