---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.FirstOrDefault``1(System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}},System.Boolean)
name: FirstOrDefault<ObjectType>(Expression<Func<ObjectType, Boolean>>, Boolean)
type: Method
summary: Searches for the first object that matches the specified lambda expression. The generic parameter determines the object's type. This method takes uncommitted changes into account.
syntax:
  content: |-
    public override ObjectType FirstOrDefault<ObjectType>(Expression<Func<ObjectType, bool>> criteriaExpression, bool inTransaction)
        where ObjectType : class
  parameters:
  - id: criteriaExpression
    type: System.Linq.Expressions.Expression{System.Func{{ObjectType},System.Boolean}}
    description: A lambda expression to search for an object.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if the method takes unsaved changes into account; otherwise, **false**.'
  typeParameters:
  - id: ObjectType
    description: The @System.Type of an object to be returned.
  return:
    type: '{ObjectType}'
    description: The first object that matches the specified lambda expression.
seealso: []
---
[!include[FirstOrDefault_ExampleDescription](~/templates/FirstOrDefault_ExampleDescription.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Xpo;
using DevExpress.Persistent.Base;
using System.Diagnostics;
// ...
public class SendEmailController : ObjectViewController<ListView, Contact> {
    public SendEmailController() {
        ParametrizedAction sendEmailAction = new ParametrizedAction(
            this, "SendEmail", PredefinedCategory.Edit, typeof(string));
        sendEmailAction.Execute += SendEmailAction_Execute;
    }
    private void SendEmailAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
        XPObjectSpace objectSpace = (XPObjectSpace)View.ObjectSpace;
        string contactParamValue = e.ParameterCurrentValue as string;
        if (!string.IsNullOrEmpty(contactParamValue)) {
            Contact contact = objectSpace.FirstOrDefault<Contact>(p => p.LastName == contactParamValue, true);
            if (!string.IsNullOrEmpty(contact?.Email)) {
                Process.Start($"mailto:{contact.Email}");
            }
        }
    }
}
```
***
