---
uid: "112920"
seealso: []
title: Create a New Object using the Navigation Control
---
# Create a New Object using the Navigation Control
This topic demonstrates executing custom code on a specific [navigation item](xref:113198) click. A navigation item that invokes the Detail View in Edit mode for an **Issue** object is added to the Navigation control.

![CreateObjectFromNavigationControl](~/images/createobjectfromnavigationcontrol116018.png)

> [!Tip]
> A complete sample project is available in the following GitHub Example: [XAF - How to Show a New Object Detail View via the Navigation Control](https://github.com/DevExpress-Examples/xaf-how-to-show-a-new-object-detail-view-via-the-navigation-control).

In this example, the following `Issue` persistent class is used for demo purposes. You can use any other persistent class.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions, ImageName("BO_List")]
public class Issue : BaseObject {
    public virtual string Subject { get; set; }
    [FieldSize(FieldSizeAttribute.Unlimited)]
    public virtual string Description { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
// ...
[DefaultClassOptions, ImageName("BO_List")]
public class Issue : BaseObject {
    public Issue(Session session) : base(session) { }
    private string subject;
    public string Subject {
        get { return subject; }
        set { SetPropertyValue(nameof(Subject), ref subject, value); }
    }
    private string description;
    [Size(SizeAttribute.Unlimited)]
    public string Description {
        get { return description; }
        set { SetPropertyValue(nameof(Description), ref description, value); }
    }
}
```
***

To create a new object using the Navigation control, add a new navigation item and specify the code to be executed on this item click.

## Add a new Navigation Item
To add a new navigation item, invoke the [Model Editor](xref:112582) for the module project by double-clicking the _Model.DesignedDiffs.xafml_ file. Find the **Issue** navigation item node and add a new node to the same navigation group.

For this node, specify the properties from the table below with the corresponding values:

| Property | Value |
|---|---|
| [IModelBaseChoiceActionItem.Id](xref:DevExpress.ExpressApp.Model.IModelBaseChoiceActionItem.Id) | **NewIssue** |
| [IModelBaseChoiceActionItem.Caption](xref:DevExpress.ExpressApp.Model.IModelBaseChoiceActionItem.Caption) | **Create New Issue…** |
| [IModelBaseChoiceActionItem.ImageName](xref:DevExpress.ExpressApp.Model.IModelBaseChoiceActionItem.ImageName) | **Action_New** |
| [IModelNavigationItem.View](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.View) | **Issue_DetailView** |

![CreateObjectFromNavigationControl_ME](~/images/createobjectfromnavigationcontrol_me116662.png)

Refer to the [Add an Item to the Navigation Control](xref:402131) topic to learn more about creating navigation items in the Model Editor.

## Specify the Code to be Executed on a Navigation Item Click
To specify the code to be executed when the **Create New Issue…** navigation item is clicked, follow the steps below:

1. Create a Controller that is the [](xref:DevExpress.ExpressApp.WindowController) descendant, override the **OnActivated** method, and subscribe to the [ShowNavigationItemController.CustomShowNavigationItem](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomShowNavigationItem) event in this method. Use the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method to access the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController) instance.
2. In the `CustomShowNavigationItem` event handler, access the current navigation item identifier using the [CustomShowNavigationItemEventArgs.ActionArguments](xref:DevExpress.ExpressApp.SystemModule.CustomShowNavigationItemEventArgs.ActionArguments) event argument.
3. If the identifier is "NewIssue", create the following objects using the corresponding methods from the table below: 
	
	| Object | Method |
	|---|---|
	| Object Space | [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) |
	| **Issue** object | [IObjectSpace.CreateObject](xref:DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type)) |
	| Detail View for the **Issue** object | [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) |
4. Specify that the Detail View should be displayed using the [ShowViewParameters.CreatedView](xref:DevExpress.ExpressApp.ShowViewParameters.CreatedView) property.
5. Since the Navigation control is displayed in the main [Window](xref:112608) only, the created Controller should be activated for the main Window as well by setting the [WindowController.TargetWindowType](xref:DevExpress.ExpressApp.WindowController.TargetWindowType) property to **Main** in the Controller's constructor.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
// ...
public class NewObjectFromNavigationController : WindowController {
    public NewObjectFromNavigationController() {
        TargetWindowType = WindowType.Main;
    }
    protected override void OnActivated() {
        base.OnActivated();
        ShowNavigationItemController showNavigationItemController = Frame.GetController<ShowNavigationItemController>();
        showNavigationItemController.CustomShowNavigationItem += showNavigationItemController_CustomShowNavigationItem;
    }
    void showNavigationItemController_CustomShowNavigationItem(object sender, CustomShowNavigationItemEventArgs e) {
        if (e.ActionArguments.SelectedChoiceActionItem.Id == "NewIssue") {
            IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Issue));
            Issue newIssue = objectSpace.CreateObject<Issue>();
            DetailView detailView = Application.CreateDetailView(objectSpace, newIssue);
            e.ActionArguments.ShowViewParameters.CreatedView = detailView;
            e.Handled = true;
        }
    }
}
```
***

Run the WinForms or ASP.NET Core Blazor application to check that the `Issue` objects can be created using the **Create New Issue…** navigation item (see the image at the beginning of this topic).
