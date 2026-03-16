---
uid: DevExpress.ExpressApp.IObjectSpace.FirstOrDefault``1(System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}})
name: FirstOrDefault<ObjectType>(Expression<Func<ObjectType, Boolean>>)
type: Method
summary: Searches for the first object that matches the specified lambda expression. The generic parameter determines the object's type.
syntax:
  content: |-
    ObjectType FirstOrDefault<ObjectType>(Expression<Func<ObjectType, bool>> criteriaExpression)
        where ObjectType : class
  parameters:
  - id: criteriaExpression
    type: System.Linq.Expressions.Expression{System.Func{{ObjectType},System.Boolean}}
    description: A lambda expression to search for an object.
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
        IObjectSpace objectSpace = View.ObjectSpace;
        string contactParamValue = e.ParameterCurrentValue as string;
        if (!string.IsNullOrEmpty(contactParamValue)) {
            Contact contact = objectSpace.FirstOrDefault<Contact>(p => p.LastName == contactParamValue);
            if (!string.IsNullOrEmpty(contact?.Email)) {
                Process.Start($"mailto:{contact.Email}");
            }
        }
    }
}
```
***

Do not implement this method when you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in a [](xref:DevExpress.ExpressApp.BaseObjectSpace) descendant. The [BaseObjectSpace.FirstOrDefault\<ObjectType>(Expression\<Func\<ObjectType, Boolean>>)](xref:DevExpress.ExpressApp.BaseObjectSpace.FirstOrDefault``1(System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}})) method invokes a public virtual [BaseObjectSpace.FirstOrDefault\<ObjectType>(Expression\<Func\<ObjectType, Boolean>>, Boolean)](xref:DevExpress.ExpressApp.BaseObjectSpace.FirstOrDefault``1(System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}},System.Boolean)) method. Override the public virtual **BaseObjectSpace.FirstOrDefault** method to implement an object search.