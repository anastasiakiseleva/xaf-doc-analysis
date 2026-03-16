---
uid: DevExpress.ExpressApp.Editors.StaticText
name: StaticText
type: Class
summary: An abstract class that serves as the base class for the Static Text [View Items](xref:112612).
syntax:
  content: 'public abstract class StaticText : ViewItem, IAppearanceFormat, IAppearanceBase, IAppearanceVisibility, INotifyAppearanceVisibilityChanged'
seealso:
- linkId: DevExpress.ExpressApp.Editors.StaticText._members
  altText: StaticText Members
- linkId: "112612"
- linkId: DevExpress.ExpressApp.Editors.StaticImage
- linkId: DevExpress.ExpressApp.Editors.ViewItemAttribute
---
A Static Text View Item is used to display a particular caption in a UI. The `StaticText` class is an abstract class from which all the Static Text View Items  derive. The following table lists XAF's built-in Static Text View Items.

| StaticText Descendant | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.Win.Editors.StaticTextViewItem) (DevExpress.ExpressApp.Win.Editors) | The Static Text View Item used in XAF Windows Forms applications. |
| [](xref:DevExpress.ExpressApp.Blazor.Editors.StaticTextViewItem) (DevExpress.ExpressApp.Blazor.Editors) | The Static Text View Item used in XAF ASP.NET Core Blazor applications. |

To extend the built-in functionality and use a specific text-display control, you may need to implement a custom Static Text View Item. To do this, override the protected virtual `CreateControlCore` method to instantiate the required control. Apply the [](xref:DevExpress.ExpressApp.Editors.ViewItemAttribute) to the custom item to make a new child node appear in the **ViewItems** node of the Application Model. For more information, refer to the [](xref:405483) topic and [](xref:DevExpress.ExpressApp.Editors.ViewItem) class description. Note that a custom Static Text View Item should be implemented in a platform-specific [application project](xref:118045). This View Item is loaded into the Application Model and is available for use in the UI. 

The `StaticText` class implements the [](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat) interface so that the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) can change the appearance format according to [conditional appearance rules](xref:113286) applied to a StaticText View Item.

For information on how to implement a Static Text View Item, refer to the following topic: [How to: Implement a View Item](xref:405483).