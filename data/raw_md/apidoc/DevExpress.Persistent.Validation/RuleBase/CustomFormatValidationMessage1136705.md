---
uid: DevExpress.Persistent.Validation.RuleBase.CustomFormatValidationMessage
name: CustomFormatValidationMessage
type: Event
summary: Occurs when the validation result message is being formatted.
syntax:
  content: public static event EventHandler<CustomFormatValidationMessageEventArgs> CustomFormatValidationMessage
seealso: []
---
Handle this event to apply custom formatting to the validation result message. Use the handler's **Object** parameter to access the object that is being validated, **MessageFormat** - to access the error message template, and **ResultMessage** - to specify the resulting message. Set the handler's **Handled** parameter to **true** to cancel the default formatting.

The following Controller replaces the property name with the corresponding View Item caption in the validation message of the "MyRule" rule. This Controller activates for the **Employee** Detail View only.

# [C#](#tab/tabid-csharp)

```csharp
using System.Linq;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Model;
using DevExpress.Persistent.Validation;
// ...
namespace MySolution.Module.Controllers {
    public class CustomizeValidationMessageController : ObjectViewController<DetailView, Employee> {
        protected override void OnActivated() {
            base.OnActivated();
            RuleBase.CustomFormatValidationMessage += RuleBase_CustomFormatValidationMessage;
        }
        private void RuleBase_CustomFormatValidationMessage(object sender, CustomFormatValidationMessageEventArgs e) {
            RuleBase rule = (RuleBase)sender;
            if (!e.Handled && rule.Id == "MyRule" && e.Object is Employee) {
                string propertyCaption = rule.UsedProperties[0];
                IModelViewItem modelViewItem = View.Model.Items.FirstOrDefault(x => x.Id == propertyCaption);
                propertyCaption = (modelViewItem == null) ? propertyCaption : modelViewItem.Caption;
                e.ResultMessage = e.MessageFormat.Replace("{TargetPropertyName}", propertyCaption);
                e.Handled = true;
            }
        }
        protected override void OnDeactivated() {
            base.OnDeactivated();
            RuleBase.CustomFormatValidationMessage -= RuleBase_CustomFormatValidationMessage;
        }
    }
}
```
# [VB.NET](#tab/tabid-vb)

```vb
Imports System.Linq
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Model
Imports DevExpress.Persistent.Validation
' ...
Namespace MySolution.Module.Controllers
    Public Class CustomizeValidationMessageController
        Inherits ObjectViewController(Of DetailView, Employee)

        Protected Overrides Sub OnActivated()
            MyBase.OnActivated()
            AddHandler RuleBase.CustomFormatValidationMessage, AddressOf RuleBase_CustomFormatValidationMessage
        End Sub
        Private Sub RuleBase_CustomFormatValidationMessage(ByVal sender As Object, ByVal e As CustomFormatValidationMessageEventArgs)
            Dim rule As RuleBase = DirectCast(sender, RuleBase)
            If Not e.Handled AndAlso rule.Id = "MyRule" AndAlso TypeOf e.Object Is Employee Then
                Dim propertyCaption As String = rule.UsedProperties(0)
                Dim modelViewItem As IModelViewItem = View.Model.Items.FirstOrDefault(Function(x) x.Id = propertyCaption)
                propertyCaption = If(modelViewItem Is Nothing, propertyCaption, modelViewItem.Caption)
                e.ResultMessage = e.MessageFormat.Replace("{TargetPropertyName}", propertyCaption)
                e.Handled = True
            End If
        End Sub
        Protected Overrides Sub OnDeactivated()
            MyBase.OnDeactivated()
            RemoveHandler RuleBase.CustomFormatValidationMessage, AddressOf RuleBase_CustomFormatValidationMessage
        End Sub
    End Class
End Namespace
```

***

If you want to customize this message for all Views in the application, subscribe to this event in the [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup(DevExpress.ExpressApp.XafApplication)) method.