---
uid: DevExpress.ExpressApp.Editors.ActionContainerViewItem
name: ActionContainerViewItem
type: Class
summary: An abstract class that serves as the base class for the Action Container [View Items](xref:112612).
syntax:
  content: 'public abstract class ActionContainerViewItem : ViewItem, IActionContainer, ISupportUpdate, IDisposable, IAppearanceVisibility, IAppearanceBase, INotifyAppearanceVisibilityChanged'
seealso:
- linkId: DevExpress.ExpressApp.Editors.ActionContainerViewItem._members
  altText: ActionContainerViewItem Members
- linkId: DevExpress.ExpressApp.Editors.ViewItemAttribute
---
An Action Container View Item is used to display a particular [Action Container](xref:112610) in a UI. The `ActionContainerViewItem` class is an abstract class from which all the Action Container View Items derive. The following table lists XAF's built-in Action Container View Items.

| ActionContainerViewItem Descendant | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.Blazor.Editors.BlazorActionContainerViewItem) | The Action Container View Item used in the XAF ASP.NET Core Blazor applications. |
| [](xref:DevExpress.ExpressApp.Win.Editors.WinActionContainerViewItem) | The Action Container View Item used in the XAF Windows Forms applications. |

The `ActionContainerViewItem` exposes the [ActionContainerViewItem.BeginUpdate](xref:DevExpress.ExpressApp.Editors.ActionContainerViewItem.BeginUpdate) and [ActionContainerViewItem.EndUpdate](xref:DevExpress.ExpressApp.Editors.ActionContainerViewItem.EndUpdate) methods designed to implement batch modifications with Action Container View Items. Use them to prevent excessive updates when changing multiple settings at once. For this purpose, enclose the code that changes multiple properties within calls to these methods.

For information on adding an Action Container View Item to a Detail View, refer to the following topics:
* [View Items](xref:112612)
* [How to: Include an Action to a Detail View Layout](xref:112816)