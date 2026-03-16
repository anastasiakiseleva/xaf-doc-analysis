---
uid: DevExpress.ExpressApp.Win.WinApplication.CustomHandleException
name: CustomHandleException
type: Event
summary: Occurs before displaying a message box with an exception message.
syntax:
  content: public event EventHandler<CustomHandleExceptionEventArgs> CustomHandleException
seealso: []
---
Raised as the result of executing the [WinApplication.HandleException](xref:DevExpress.ExpressApp.Win.WinApplication.HandleException(System.Exception)) method. Handle the **CustomHandleException** event to customize the exceptions processing in a Windows Forms application. Place a custom code in this event handler, and it will be executed before the message box is shown. The exception that occurs is accessible via the **Exception** parameter. You can set the handler's **Handled** parameter, to prohibit displaying the default message box.

# [C#](#tab/tabid-csharp)

```csharp
static class Program {
    static void Main() {
        // ...
        MySolutionWindowsFormsApplication winApplication = 
            new MySolutionWindowsFormsApplication();
        //...
        winApplication.CustomHandleException += winApplication_CustomHandleException;
        // ...
        try {
            winApplication.Setup();
            winApplication.Start();
        }
        catch (Exception e) {
            winApplication.HandleException(e);
        }
    }
    // ...
    static void winApplication_CustomHandleException(
        object sender, CustomHandleExceptionEventArgs e) {
        // Place your code here. Set e.Handled to true to prohibit displaying default message box.
    }
}
```
***