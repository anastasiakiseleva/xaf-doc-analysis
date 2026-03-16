---
uid: DevExpress.ExpressApp.SystemModule.NewObjectViewController.ObjectCreating
name: ObjectCreating
type: Event
summary: Occurs before creating a new object of the type selected in the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s control.
syntax:
  content: public event EventHandler<ObjectCreatingEventArgs> ObjectCreating
seealso: []
---
This event can be handled to do the following:

* Cancel creating a new object. For this purpose, set the event hander's **ObjectCreatingEventArgs.Cancel** parameter to **true**. By default, it is set to **false**.
* Cancel invoking the Detail View for initialization of the newly created object. For this purpose, set the event handler's **ObjectCreatingEventArgs.ShowDetailView** parameter to **false**. By default, it is set to **true**.
* Create the new object yourself. For this purpose, use the [](xref:DevExpress.ExpressApp.IObjectSpace) object passed as the handler's **ObjectCreatingEventArgs.ObjectSpace** parameter. To pass the newly created object to the system, set it for the handler's **ObjectCreatingEventArgs.NewObject** parameter.

To determine the type of the object to be created, use the handler's [ObjectCreatingEventArgs.ObjectType](xref:DevExpress.ExpressApp.SystemModule.ObjectCreatingEventArgs.ObjectType) parameter.

> [!NOTE]
> The **WebApplication.OptimizationSettings.AllowFastProcessObjectsCreationActions** option can influence the **ObjectCreating** event. Disable this option as described in the [Faster rendering and other performance optimizations for popular Web UI scenarios in XAF](https://supportcenter.devexpress.com/Ticket/Details/T386142/faster-rendering-and-other-performance-optimizations-for-popular-web-ui-scenarios-in-xaf) KB article, if you face any difficulty when custom processing selected items is implemented in this event handler (e.g., difficulty with the default UI elements rendering or behavior).

To see an example of how to handle the **ObjectCreating** event, refer to the [How to: Limit the Amount of Objects Created using the New Action](xref:112913) topic.
