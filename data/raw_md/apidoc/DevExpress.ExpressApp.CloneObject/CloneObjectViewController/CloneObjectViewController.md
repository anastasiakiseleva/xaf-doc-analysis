---
uid: DevExpress.ExpressApp.CloneObject.CloneObjectViewController
name: CloneObjectViewController
type: Class
summary: A [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **Clone** action.
syntax:
  content: 'public class CloneObjectViewController : ObjectViewController, ICreateObjectActionProvider'
seealso:
- linkId: DevExpress.ExpressApp.CloneObject.CloneObjectViewController._members
  altText: CloneObjectViewController Members
---
the [Clone Object Module](xref:112835) provides the `CloneObjectViewController` Controller. This Controller is active for List and Detail [Views](xref:112611).

To access the **Clone** Action used to clone the currently selected object, use the [CloneObjectViewController.CloneObjectAction](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CloneObjectAction) property. For more information on how this Action works and how it can be customized, refer to the property's description.

![XAF Clone Object Module in Windows Forms and ASP.NET Core Blazor, DevExpress](~/images/cloneobject.png)

Additionally, you can subscribe to events exposed by the `CloneObjectViewController` to perform the following customizations:

* [CloneObjectViewController.CustomCloneObject](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CustomCloneObject) - to implement custom cloning logic
* [CloneObjectViewController.CustomGetCloneActionTargetTypes](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CustomGetCloneActionTargetTypes) - to use the custom list of target types available via the **CloneObject** action;
* [CloneObjectViewController.CustomShowClonedObject](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CustomShowClonedObject) - to implement the custom code to be executed before or instead of displaying the Detail View with the cloned object.

For more information, refer to the corresponding event description.