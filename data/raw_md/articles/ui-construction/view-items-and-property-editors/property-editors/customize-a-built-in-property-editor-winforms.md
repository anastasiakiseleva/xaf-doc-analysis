---
uid: "113104"
title: 'Customize a Built-in Property Editor (WinForms)'
seealso:
- linkId: "402188"
- linkId: "113097"
- linkId: "402154"
- linkId: "120092"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-win-custom-button-in-lookup-property-editor
  altText: 'GitHub Example: XAF WinForms - Add a custom button into LookupPropertyEditor'
---
# Customize a Built-in Property Editor (WinForms)

This topic describes how to access a built-in XAF Property Editor in a Windows Forms application.

In this example, the `DatePropertyEditor` is customized to display a calendar and a clock.

![A Custom Calendar Property Editor in a Windows Forms Application](~/images/custompropertyeditor2116096.png)

[!include[<built-in and custom property editors>](~/templates/main-demo-tip.md)]

## Inherit the Property Editor

Create a new class in the _MySolution\Win\Editors_ folder. [!include[PublicEditor](~/templates/publiceditor111797.md)]

Inherit the newly created class from the `DatePropertyEditor` class. Since this class is a [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) class descendant, you can use a [repository item](xref:114580#editor-architecture-repositories-and-repository-items) to access its settings. To customize the controls created in Detail and List Views, override the `SetupRepositoryItem` method.

To use the customized Property Editor with [](xref:System.DateTime) type properties, apply the [PropertyEditor](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute) attribute as demonstrated in the code sample below.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Utils;
using DevExpress.XtraEditors.Repository;
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Win.Editors;
//...
[PropertyEditor(typeof(DateTime), false)]
public class CustomDateTimeEditor : DatePropertyEditor {
    public CustomDateTimeEditor(Type objectType, IModelMemberViewItem info) : 
        base(objectType, info) { }
    protected override void SetupRepositoryItem(RepositoryItem item) {
        base.SetupRepositoryItem(item);
        RepositoryItemDateTimeEdit dateProperties = (RepositoryItemDateTimeEdit)item;
        dateProperties.CalendarTimeEditing = DefaultBoolean.True;
        dateProperties.CalendarView = CalendarView.Vista;
    }
}
```
***

### Use the Customized Property Editor

To use the implemented Property Editor with a specific property, double-click the _MySolution\Win\Model.xamfl_ file and run the [Model Editor](xref:112582) in the Windows Forms project. Set the [IModelCommonMemberViewItem.PropertyEditorType](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType) property of the required **OwnMember** or **ViewItem** node to `CustomDateTimeEditor`.

> [!TIP]
> [!include[DefaultEditor](~/templates/defaulteditor111198.md)] The [CompositeView.GetItems\<T>](xref:DevExpress.ExpressApp.CompositeView.GetItems``1) method allows you to use a custom Property Editor with all properties instead of the default Property Editor.

[!include[AdjustFormatting](~/templates/adjustformatting111199.md)]

## Customize a Built-in Property Editor in a Controller

Create a new Controller in the in the _MySolution\Win\Controllers_ folder..

To customize the Property Editor's control, override the `OnActivated` method and use the `CustomizeViewItemControl` method.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
using DevExpress.XtraEditors;
using YourApplication.Module.BusinessObjects;

namespace YourApplication.Module.Win.Controllers {
    public partial class WinDateEditCalendarController : ObjectViewController<DetailView, TargetClassName> {
        public WinDateEditCalendarController() {
            InitializeComponent();
        }
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<DatePropertyEditor>(this, SetCalendarView, nameof(TargetClassName.PropertyName));
        }
        private void SetCalendarView(DatePropertyEditor propertyEditor) {
            DateEdit dateEdit = propertyEditor.Control;
            dateEdit.Properties.CalendarView = DevExpress.XtraEditors.Repository.CalendarView.TouchUI;
        }
    }
}
```
[`CustomizeViewItemControl`]: xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl*

