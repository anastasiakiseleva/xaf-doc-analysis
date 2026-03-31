---
uid: "112825"
seealso:
- linkId: "402159"
- linkId: DevExpress.ExpressApp.Utils.EnumDescriptor
- linkId: 112792
- linkId: DevExpress.ExpressApp.Utils.ImageLoader
title: 'How to: Set Images and Captions for Enumeration Values'
---

# How to: Set Images and Captions for Enumeration Values

This topic describes how to associate custom SVG or raster images with enumeration values and specify captions for these values.

For information on how to add and override UI images, refer to the [Add and Replace Icons](xref:112792) topic.

## Enumeration as a Property Type

Use the [](xref:DevExpress.Persistent.Base.ImageNameAttribute) to set an image that represents an enumeration value in UI. Apply this attribute to the enumeration values and specify the images:

# [C#](#tab/tabid-csharp)

```csharp
public enum SampleEnum {	
    [ImageName("BO_Person")]
    First,	
    [ImageName("BO_Position")]
    Second,	
    [ImageName("BO_Employee")]
    Third 
}
```
***

ASP.NET Core Blazor
:   ![Enumeration Images, ASP.NET Core Blazor, DevExpress](~/images/blazor-enum-images-devexpress.png)
Windows Forms
:   ![Enumeration Images, Windows Forms, DevExpress](~/images/enumimages116368.png)

> [!NOTE]
> Use the same image format for all items in one collection: either SVG or raster. Otherwise, an enumeration property editor may not show certain images. If you observe such behavior in your application, make sure image files for all entries have the same format and check the application's log file for any additional diagnostic message the enumeration property editor may have recorded.

Use the [](xref:DevExpress.ExpressApp.DC.XafDisplayNameAttribute) to set a caption that represents an enumeration value in UI. Apply this attribute to the enumeration values and specify the captions:

# [C#](#tab/tabid-csharp)

```csharp
public enum SampleEnum {	
    [XafDisplayName("John")]
    First,	
    [XafDisplayName("Sam")]
    Second,	
    [XafDisplayName("Bob")]
    Third 
}
```
***

ASP.NET Core Blazor
:   ![Enumeration Captions, ASP.NET Core Blazor, DevExpress](~/images/blazor-enum-captions-devexpress.png)
Windows Forms
:   ![Enumeration Captions, Windows Forms, DevExpress](~/images/enumcaptions116720.png)

## Enumeration as Option Source for a Single Choice Action

Enumeration values can represent items in a Single Choice Action's drop-down menu. The following code demonstrates how to populate the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection with enumeration values and associate images with these items:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Utils;
using DevExpress.Persistent.Base;
using YourSolutionName.Module.BusinessObjects;

namespace YourSolutionName.Module.Controllers {
    public partial class TaskActionsController : ViewController {
        public TaskActionsController() {
            var SetPriorityAction = new SingleChoiceAction(this, "myAction1", PredefinedCategory.Edit);
            SetPriorityAction.ImageName = "Task";
            SetPriorityAction.ItemType = SingleChoiceActionItemType.ItemIsOperation;
            foreach (SampleEnum current in Enum.GetValues(typeof(SampleEnum))) {
                EnumDescriptor ed = new EnumDescriptor(typeof(SampleEnum));
                ChoiceActionItem item = new ChoiceActionItem(ed.GetCaption(current), current);
                item.ImageName = ImageLoader.Instance.GetEnumValueImageName(current);
                SetPriorityAction.Items.Add(item);
            }
        }
    }
}
```
***

The following image displays the `SetPriorityAction`:

ASP.NET Core Blazor
:   ![|Enumeration Values as SingleChoiceAction Items, ASP.NET Core Blazor, DevExpress|](~/images/settaskpriority-caption-image-blazor-devexpress.png)
Windows Forms
:   ![|Enumeration Values as SingleChoiceAction Items, Windows Forms, DevExpress|](~/images/imagesforenum_7115615.png)
