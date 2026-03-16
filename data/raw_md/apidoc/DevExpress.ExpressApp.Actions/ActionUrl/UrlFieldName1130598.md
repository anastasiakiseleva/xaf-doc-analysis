---
uid: DevExpress.ExpressApp.Actions.ActionUrl.UrlFieldName
name: UrlFieldName
type: Property
summary: Specifies the name of a persistent object's property whose value is used to build a URL text based on the [ActionUrl.UrlFormatString](xref:DevExpress.ExpressApp.Actions.ActionUrl.UrlFormatString) property value.
syntax:
  content: public string UrlFieldName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value representing a persistent object's property specifying a URL.
seealso: []
---
An [](xref:DevExpress.ExpressApp.Actions.ActionUrl) Action can be used to load a page specified by a particular property of a persistent object.The following code demonstrates how this is done:

# [C#](#tab/tabid-csharp)

```csharp
public class DomainObject1 : BaseObject {
   //...
   private string webSite;
   public string WebSite {
      get { return webSite; }
      set { SetPropertyValue(ref webSite, value); }
   }
}
public partial class ViewController1 : ViewController{
   private void InitializeComponent(){
      //...
      this.urlAction1 = new DevExpress.ExpressApp.Actions.ActionUrl(this.components);
      this.urlAction1.UrlFieldName = "WebSite";
      this.urlAction1.UrlFormatString = "http://{0}";
      //...
   }
}
```
***

In this instance, the ActionUrl should be activated in a Detail View or for each object in a List View. To do that, set the [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property to [SelectionDependencyType.RequireSingleObject](xref:DevExpress.ExpressApp.Actions.SelectionDependencyType.RequireSingleObject) and the [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property to "RecordEdit". In a List View, the Action will be displayed in an additional cell for each object.

![TextFormatString2](~/images/textformatstring2115618.png)

To learn how to specify a caption for an ActionUrl, refer to the [ActionUrl.TextFormatString](xref:DevExpress.ExpressApp.Actions.ActionUrl.TextFormatString) property definition.

If the **UrlFieldName** property is not empty, the Action's [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property is set to the [SelectionDependencyType.RequireSingleObject](xref:DevExpress.ExpressApp.Actions.SelectionDependencyType.RequireSingleObject) value. So, to make this Action available for a List View, the Action Container specified by its [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) should be contained in the required Template, and the List View must have a single selected object.