---
uid: DevExpress.ExpressApp.ViewShortcut
name: ViewShortcut
type: Class
summary: Supplies key information on a [View](xref:112611).
syntax:
  content: 'public class ViewShortcut : LightDictionary<string, string>'
seealso:
- linkId: DevExpress.ExpressApp.ViewShortcut._members
  altText: ViewShortcut Members
---
A View Shortcut is a dictionary containing key/value pairs describing a View. Each key names a parameter describing a View, and has the associated value. For example, by default, a View Shortcut contains a key corresponding to the View identifier, the type of the object(s) displayed by the View, the key property value of the object displayed by the View and so on. This information is used to recreate a particular View in the future.

To create a View Shortcut, use the [View.CreateShortcut](xref:DevExpress.ExpressApp.View.CreateShortcut) method. To recreate a View based on the information provided by the View Shortcut, use the [XafApplication.ProcessShortcut](xref:DevExpress.ExpressApp.XafApplication.ProcessShortcut(DevExpress.ExpressApp.ViewShortcut)) method. You can add custom key/value pairs to View Shortcuts when they are created, by handling the [View.CustomizeViewShortcut](xref:DevExpress.ExpressApp.View.CustomizeViewShortcut) event. However, generally, you should not modify values corresponding to keys already existing in just created View Shortcuts, as this information is used by XAF to support various built-in functionalities, and you can easily break it. To process custom key/value pairs when a View is recreated via the **ProcessShortcut** method, handle the [XafApplication.CustomProcessShortcut](xref:DevExpress.ExpressApp.XafApplication.CustomProcessShortcut) event.

The following help topic contains examples of using View Shortcuts.

* [How to: Implement Custom Context Navigation](xref:113200)
* [How to: Customize the New Action's Items List](xref:112915)