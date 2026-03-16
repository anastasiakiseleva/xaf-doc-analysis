---
uid: DevExpress.ExpressApp.Win.WinApplication.HandleException(System.Exception)
name: HandleException(Exception)
type: Method
summary: Shows the message box with details on the specified exception.
syntax:
  content: public void HandleException(Exception e)
  parameters:
  - id: e
    type: System.Exception
    description: A **System.Exception** object representing an exception that occurred.
seealso: []
---
Triggers the [WinApplication.CustomHandleException](xref:DevExpress.ExpressApp.Win.WinApplication.CustomHandleException) event. If the event's **Handled** parameter is not set to **true**, the message box is displayed via the [Messaging.Show](xref:DevExpress.ExpressApp.Win.Core.Messaging.Show*) method (an overload that takes the _caption_ and _exception_ parameters is used).

The **HandleException** method is called each time an exception occurs when running a Windows Forms application (see the snippet from the **Program.Main** method below).

# [C#](#tab/tabid-csharp)

```csharp
static void Main() {
    // ...
   try {
        winApplication.Setup();
        winApplication.Start();
    }
    catch (Exception e) {
        winApplication.HandleException(e);
    }
}
```
***