---
uid: DevExpress.ExpressApp.SecuritySystem.CustomIsGranted
name: CustomIsGranted
type: Event
summary: Occurs when the **PermissionRequest** instance is passed to the [SecuritySystem.IsGranted](xref:DevExpress.ExpressApp.SecuritySystem.IsGranted*) method.
syntax:
  content: public static event EventHandler<CustomHasPermissionToEventArgs> CustomIsGranted
seealso: []
---
Handle this event to provide a custom code that calculates the **IsGranted** result. To override the default code, set the **Handled** to **true** and assign a custom result to the [CustomHasPermissionToEventArgs.Result](xref:DevExpress.ExpressApp.CustomHasPermissionToEventArgs.Result) parameter.

# [C#](#tab/tabid-csharp)

```csharp
SecuritySystem.CustomIsGranted += delegate (object sender, CustomHasPermissionToEventArgs e) {
    if (e.Operation == SecurityOperations.Write ||
        e.Operation == SecurityOperations.Delete ||
        e.Operation == SecurityOperations.Create) {
        e.Result = false;
        e.Handled = true;
    }
};
```
***

As the **CustomIsGranted** event is static, you can subscribe to it from any place in your code which is executed before a user is logged on, e.g.:

[!include[CodeLocationsBeforeLogon](~/templates/codelocationsbeforelogon111430.md)]

The **CustomIsGranted** event is not raised when:

* evaluating a navigation permission specified via the Role's [Navigation Permissions](xref:113366) tab;
* filtering data at the ORM level or at the application server side (in the Integrated or Middle-Tier security mode);
* calling the **SecuritySystem.Instance.IsGranted** method instead of **SecuritySystem.IsGranted**;
* passing the custom [](xref:DevExpress.ExpressApp.Security.IPermissionRequest) request object which does not inherit **PermissionRequest** to the **IsGranted** method.