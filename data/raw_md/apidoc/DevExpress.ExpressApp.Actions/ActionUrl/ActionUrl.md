---
uid: DevExpress.ExpressApp.Actions.ActionUrl
name: ActionUrl
type: Class
summary: An [Action](xref:112622) which is used to redirect a browser to a specified page.
syntax:
  content: 'public class ActionUrl : ActionBase'
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionUrl._members
  altText: ActionUrl Members
---
The `ActionUrl` class inherits the basic [Action](xref:112622) functionality from the [](xref:DevExpress.ExpressApp.Actions.ActionBase) class. XAF only supports URL Actions in ASP.NET Core Blazor applications.

Use `ActionUrl` to invoke a browser and pass a URL to it. To specify link anchor text, use the [ActionUrl.TextFormatString](xref:DevExpress.ExpressApp.Actions.ActionUrl.TextFormatString) property. To specify the URL, use the [ActionUrl.UrlFormatString](xref:DevExpress.ExpressApp.Actions.ActionUrl.UrlFormatString) property. To use a property value within the URL or anchor text, use [ActionUrl.UrlFieldName](xref:DevExpress.ExpressApp.Actions.ActionUrl.UrlFieldName) and [ActionUrl.TextFieldName](xref:DevExpress.ExpressApp.Actions.ActionUrl.TextFieldName) properties. See property descriptions for more information about associated restrictions.

The `ActionUrl`can be visualized by any of the following ASP.NET Core Blazor controls:
* A Toolbar item
* A Grid column
* A Grid row's context menu

For more information, refer to the following topic: [Action Containers](xref:112610).

A List View can display an action in an additional column. Each cell displays a link that uses corresponding row/object data. In such cases, you can use `UrlFieldName` and `TextFieldName` properties to specify data-driven link content. 

The following example configures an `ActionUrl` object to display hyperlinks in an additional grid column:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
// ...
public class ActionUrlController : ViewController {
    ActionUrl urlAction;

    public ActionUrlController() {
        urlAction = new ActionUrl(this, "ShowUrlAction", "ListView");
        urlAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        urlAction.UrlFieldName = "Text";
        urlAction.UrlFormatString = "http://www.google.com/?q={0}";
        urlAction.TextFormatString = "Caption for {0}";
        urlAction.TextFieldName = "Text";
    }
}
```

Alternatively, you can use the **ActionUrl** Action to show a static URL that is independent from selected objects:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
// ...
public class ActionUrlController : ViewController {
    ActionUrl urlAction;

    public ActionUrlController() {
        urlAction = new ActionUrl(this, "ShowUrlAction", "RecordEdit");
        urlAction.SelectionDependencyType = SelectionDependencyType.Independent;
        urlAction.UrlFormatString = "http://www.google.com/";
    }
}

```

The `ActionUrl` class is not designed for other scenarios.
