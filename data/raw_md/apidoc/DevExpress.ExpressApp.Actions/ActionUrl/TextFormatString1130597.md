---
uid: DevExpress.ExpressApp.Actions.ActionUrl.TextFormatString
name: TextFormatString
type: Property
summary: Specifies a caption used when an [](xref:DevExpress.ExpressApp.Actions.ActionUrl) is displayed in a List View's grid editor.
syntax:
  content: public string TextFormatString { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that represents a caption.
seealso: []
---
In ASP.NET Core Blazor applications, the `ActionUrl` associated with a selected List View item displays the link in the column with other actions (in that Action Container).

![Text Format String - Blazor](~/images/text-format-string-blazor.png)

The `TextFormatString` property specifies column cell display text.

You can insert a property value into the link anchor text. Use [ActionUrl.TextFieldName](xref:DevExpress.ExpressApp.Actions.ActionUrl.TextFieldName) and `TextFormatString` properties as demonstrated below:

```csharp
public class DomainObject1 : BaseObject {
   //...
   private string name;
   public string Name {
      get { return name; }
      set { SetPropertyValue(ref name, value); }
   }
}
public partial class ViewController1 : ViewController{
   private void InitializeComponent(){
      //...
      this.urlAction1 = new DevExpress.ExpressApp.Actions.ActionUrl(this.components);
      this.urlAction1.TextFieldName = "Name";
      this.urlAction1.TextFormatString = "Go to {0}'s site";
      //...
   }
}
```

The following image demonstrates how the `urlAction1` from the code above is displayed in the `DomainObject1` List View:

![TextFormatString2](~/images/textformatstring2115618.png)

In ASP.NET Core Blazor applications, to display an Action in an additional List View column, set [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) to [SelectionDependencyType.RequireSingleObject](xref:DevExpress.ExpressApp.Actions.SelectionDependencyType.RequireSingleObject) and [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property to `ListView`, `Edit`, or `RecordEdit`. In a List View, the Action is displayed in the same column as other Actions in the same Action Container.
