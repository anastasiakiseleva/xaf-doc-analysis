---
uid: DevExpress.ExpressApp.Win.Core.Messaging.ConfirmationDialogClosed
name: ConfirmationDialogClosed
type: Event
summary: Occurs after the confirmation dialog is closed.
syntax:
  content: public static event EventHandler<ConfirmationDialogClosedEventArgs> ConfirmationDialogClosed
seealso: []
---
The **ConfirmationDialogClosed** event is raised when executing the [Messaging.Show](xref:DevExpress.ExpressApp.Win.Core.Messaging.Show*) method. Handle this event to perform custom actions after the confirmation dialog is closed. Use the handler's [ConfirmationDialogClosedEventArgs.DialogResult](xref:DevExpress.ExpressApp.Win.Core.ConfirmationDialogClosedEventArgs.DialogResult) parameter to get the user choice.

# [C#](#tab/tabid-csharp)

```csharp
static class Program {
    static void Main() {
        // ...
        Messaging.ConfirmationDialogClosed += Messaging_ConfirmationDialogClosed;
        // ...
        winApplication.Setup();
        winApplication.Start();
        // ...
    }
    static void Messaging_ConfirmationDialogClosed(\
        object sender, ConfirmationDialogClosedEventArgs e) {
        // Place your code here. Use e.DialogResult value as required.
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Friend NotInheritable Class Program
    Private Sub New()
    End Sub
    Shared Sub Main()
        ' ...
        AddHandler Messaging.ConfirmationDialogClosed, AddressOf Messaging_ConfirmationDialogClosed
        ' ...
        winApplication.Setup()
        winApplication.Start()
        ' ...
    End Sub
    Private Shared Sub Messaging_ConfirmationDialogClosed( _
    ByVal sender As Object, ByVal e As ConfirmationDialogClosedEventArgs)
        ' Place your code here. Use e.DialogResult value as required.
    End Sub
End Class
```

***

For more sophisticated customizations, implement a custom [](xref:DevExpress.ExpressApp.Win.Core.Messaging) descendant, as detailed in the [How to: Implement a Custom Messaging Class](xref:113312).