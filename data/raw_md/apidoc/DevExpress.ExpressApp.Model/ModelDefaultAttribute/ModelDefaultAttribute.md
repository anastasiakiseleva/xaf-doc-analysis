---
uid: DevExpress.ExpressApp.Model.ModelDefaultAttribute
name: ModelDefaultAttribute
type: Class
summary: Specifies default settings that are considered when generating the [Application Model](xref:112579) node related to the target.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Property | AttributeTargets.Field | AttributeTargets.Interface, Inherited = true, AllowMultiple = true)]
    public sealed class ModelDefaultAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Model.ModelDefaultAttribute._members
  altText: ModelDefaultAttribute Members
- linkId: "112701"
---
* When applied to a [business class](xref:112570), specifies the default value of the Application Model's **BOModel** | **_\<Class\>_** node property.
* When applied to a business class' member, specifies the default value of the Application Model's **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node property.

The [PropertyName](xref:DevExpress.ExpressApp.Model.ModelDefaultAttribute.PropertyName) parameter specifies the property name, and the [PropertyValue](xref:DevExpress.ExpressApp.Model.ModelDefaultAttribute.PropertyValue) specifies the string representation of the default value. Refer to the following topics to see available properties:
* [IModelClass properties](xref:DevExpress.ExpressApp.Model.IModelClass._properties) 
* [IModelMember properties](xref:DevExpress.ExpressApp.Model.IModelMember._properties)

The code below sets the **BOModel** | **DemoTask** node's **Caption** property to "Task" and **ImageName** - to "Tasks". If you customize this value in the [Model Editor](xref:112582) and later reset this customization, the values will be "Task" and "Tasks" again.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Model;
// ...
[ModelDefault("Caption", "Task"), ModelDefault("ImageName", "Tasks")]
public class DemoTask : Task {
    // ...
}
```
***

![ModelDefault attribute in Model Editor](~/images/modeldefaultattribute.png)