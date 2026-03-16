---
uid: "113200"
title: Implement Custom Context Navigation
seealso:
- linkId: 113198
---
# Implement Custom Context Navigation

The [Navigation System](xref:113198) allows you to create custom navigation items at runtime based on specific conditions (context).

This topic explains how to populate the **Help Document** item with custom child items. 

![Application with context navigation items](~/images/context-navigation-items.png)

## Step 1. Create the HelpDocument Business Class

Create the `HelpDocument` business class with `Title` and `Text` properties.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...

[DefaultClassOptions, ImageName("BO_Report")]
public class HelpDocument : BaseObject {

    public virtual string Title { get; set; }
    // A document's text can be very long, so add FieldSizeAttribute and set its value to `Unlimited`
    [FieldSize(FieldSizeAttribute.Unlimited)]
    public virtual string Text { get; set; }
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
//...
[DefaultClassOptions, ImageName("BO_Report")]
public class HelpDocument : BaseObject {

    public HelpDocument(Session session) : base(session) { }
    public string Title {
        get { return GetPropertyValue<string>(nameof(Title)); }
        set { SetPropertyValue<string>(nameof(Title), value); }
    }
    // A document's text can be very long, so add SizeAttribute and set its value to `Unlimited`
    [Size(SizeAttribute.Unlimited)]
    public string Text {
        get { return GetPropertyValue<string>(nameof(Text)); }
        set { SetPropertyValue<string>(nameof(Text), value); }
    }
}
```
***

[`FieldSize`]: xref:DevExpress.ExpressApp.DC.FieldSizeAttribute
[`FieldSizeAttribute.Unlimited`]: xref:DevExpress.ExpressApp.DC.FieldSizeAttribute.Unlimited
[`Size`]: xref:DevExpress.Xpo.SizeAttribute
[`SizeAttribute.Unlimited`]: xref:DevExpress.Xpo.SizeAttribute.Unlimited

## Step 2. Create a Controller and Subscribe to the NavigationItemCreated Event

1. Add a [Window Controller](xref:112621) to the application.
2. Subscribe to the [ShowNavigationItemController.NavigationItemCreated](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.NavigationItemCreated) event that occurs after an item is created in the navigation control and allows you to modify the item. Unsubscribe from the event to prevent memory leaks.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.SystemModule;
//...
public class TaskBasedHelpController : WindowController {
    private ShowNavigationItemController navigationController;
    protected override void OnFrameAssigned() {
        UnsubscribeFromEvents();
        base.OnFrameAssigned();
        navigationController = Frame.GetController<ShowNavigationItemController>();
        if(navigationController != null) {
            navigationController.NavigationItemCreated += navigationItemCreated;
        }
    }
    private void UnsubscribeFromEvents() {
        if(navigationController != null) {
            navigationController.NavigationItemCreated -= navigationItemCreated;
            navigationController = null;
        }
    }
    protected override void Dispose(bool disposing) {
        UnsubscribeFromEvents();
        base.Dispose(disposing);
    }
}
```

***

## Step 3. Handle the NavigationItemCreated Event

1. In the `NavigationItemCreated` event handler, add a child **Items** folder to the **Help Document** item.
2. For every `HelpDocument` object, create a [detail view](xref:112611#detail-view).
3. For every detail view, create a navigation action (<xref:DevExpress.ExpressApp.Actions.ChoiceActionItem>) that displays the detail view.
4. Add the actions in the **Items** folder.

```csharp
void navigationItemCreated(object sender, NavigationItemCreatedEventArgs e) {
    var docType = typeof(HelpDocument);
    if (((IModelNavigationItem)e.NavigationItem.Model).View is IModelListView listViewNode
        && listViewNode.Id == Application.GetListViewId(docType)) {
        var os = Application.CreateObjectSpace<HelpDocument>();
        var docs = os.GetObjects<HelpDocument>();
        if (docs.Any()) {
            var docsSubGroup = new ChoiceActionItem() { Caption = "Items", ImageName = "BO_Folder" };
            e.NavigationItem.Items.Add(docsSubGroup);
            foreach (var doc in docs) {
                var keyString = os.GetKeyValueAsString(doc);
                var shortcut = new ViewShortcut(typeof(HelpDocument), keyString, Application.GetDetailViewId(docType));
                var docItem = new ChoiceActionItem(keyString, doc.Title, shortcut) {
                    ImageName = e.NavigationItem.ImageName
                };
                docsSubGroup.Items.Add(docItem);
            }
        }
    }
}
```

> [!note] 
> This topic demonstrates a solution that does not re-create the [Navigation System](xref:113198) items after `HelpDocument` objects are modified. You can call the @DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.RecreateNavigationItems method to update the navigation item structure when modifying data.
>
> For more information, refer to the following GitHub example: [How to show the number of List View items in the Navigation Control](https://github.com/DevExpress-Examples/XAF-How-to-show-the-number-of-list-view-items-in-the-navigation-control).