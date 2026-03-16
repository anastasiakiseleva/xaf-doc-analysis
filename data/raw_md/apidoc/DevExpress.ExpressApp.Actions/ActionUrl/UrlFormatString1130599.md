---
uid: DevExpress.ExpressApp.Actions.ActionUrl.UrlFormatString
name: UrlFormatString
type: Property
summary: Specifies the URL of the page to be loaded when executing an [](xref:DevExpress.ExpressApp.Actions.ActionUrl) Action.
syntax:
  content: public string UrlFormatString { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that represents an URL.
seealso: []
---
Below is an example of using this property.

# [C#](#tab/tabid-csharp)

```csharp
public partial class ViewController1 : ViewController{
   private void InitializeComponent(){
      //...
      this.urlAction1 = new DevExpress.ExpressApp.Actions.ActionUrl(this.components);
      this.urlAction1.UrlFormatString = "https://www.yahoo.com/";
      //this.urlAction1.UrlFormatString = "error.aspx";
      //...
   }
}
```
***

You can specify a persistent object property that contains a URL value. For details, see [ActionUrl.UrlFieldName](xref:DevExpress.ExpressApp.Actions.ActionUrl.UrlFieldName).

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

In this instance, the ActionURL should be activated in a List View for each object or in a Detail View. To do that, set the [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property to the [SelectionDependencyType.RequireSingleObject](xref:DevExpress.ExpressApp.Actions.SelectionDependencyType.RequireSingleObject) value and the [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property to "RecordEdit". In a List View, the Action will be displayed in an additional cell for each object.

![TextFormatString2](~/images/textformatstring2115618.png)
