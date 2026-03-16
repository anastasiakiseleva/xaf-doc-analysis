---
uid: "402153"
title: Access the Settings of a Property Editor in a Detail View
owner: Alexey Kazakov
seealso:
  - linkId: "112621"
  - linkId: "120092"
  - linkId: "402188"
  - linkId: "402154"
---
# Access the Settings of a Property Editor in a Detail View

This lesson explains how to access editors in a [Detail View](xref:112611) and change their settings. 

The instructions below show how to make the **Birthday** property editor display a scrollable date picker in its drop-down window.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402981)
> * [](xref:402157)

## Step-by-Step Instructions

1. In the **MySolution.Blazor.Server** and **MySolution.Win** projects, add a View Controller to the _Controllers_ folder. Name the new controller _DateEditCalendarController_. Specify the controller ancestor class [](xref:DevExpress.ExpressApp.ObjectViewController`2):

   # [ASP.NET Core Blazor](#tab/tabid-csharp-blazor)

   ```csharp{5}
   using DevExpress.ExpressApp;
   using MySolution.Module.BusinessObjects;
   // ...
   namespace MySolution.Blazor.Server.Controllers {
       public class DateEditCalendarController : ObjectViewController<DetailView, Employee> {
       // ...
       }
   }
   ```

   # [Windows Forms](#tab/tabid-csharp-winforms)
   
   ```csharp{4}
   using MySolution.Module.BusinessObjects;

   namespace MySolution.Win.Controllers {
       public class DateEditCalendarController : ObjectViewController<DetailView, Employee> {
           public DateEditCalendarController() {
               //...
           }
           // ...
       }
   }
   ```
   ***

   The `DateEditCalendarController` inherits from the [](xref:DevExpress.ExpressApp.ObjectViewController`2) base class. The parameters of the base class enable the Controller only for Detail Views that display and edit `Employee` objects.

2. Override the `OnActivated` method. Use the [DetailViewExtensions.CustomizeViewItemControl](xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[])) method to access the `Birthday` property editor settings:

   # [ASP.NET Core Blazor](#tab/tabid-csharp-blazor)
    
   ```csharp
   // ...
   using DevExpress.ExpressApp.Blazor.Editors;
   
   namespace MySolution.Blazor.Server.Controllers {
       public partial class DateEditCalendarController : ObjectViewController<DetailView, Employee> {
           protected override void OnActivated() {
               base.OnActivated();
               //Access the Birthday property editor settings
               View.CustomizeViewItemControl<DateTimePropertyEditor>(this, SetCalendarView, nameof(Employee.Birthday));
           }

           private void SetCalendarView(DateTimePropertyEditor propertyEditor) {
               //Set the date picker display mode to scroll picker
               propertyEditor.ComponentModel.PickerDisplayMode = DevExpress.Blazor.DatePickerDisplayMode.ScrollPicker;
           }
       }
   }
   ```

   # [Windows Forms](#tab/tabid-csharp-winforms)
   
   ```csharp
   using DevExpress.ExpressApp;
   using DevExpress.ExpressApp.Editors;
   using DevExpress.XtraEditors;
   using MySolution.Module.BusinessObjects;

   namespace MySolution.Win.Controllers {
       //...
       public class DateEditCalendarController : ObjectViewController<DetailView, Employee> {
           public DateEditCalendarController() {
                // ...
           }
           protected override void OnActivated() {
               base.OnActivated();
               //Access the Birthday property editor settings
               View.CustomizeViewItemControl(this, SetCalendarView, nameof(Employee.Birthday));
           }
           private void SetCalendarView(ViewItem viewItem) {
               //Set the currently displayed View Item control to a drop-down calendar
               DateEdit dateEdit = (DateEdit)viewItem.Control;
               //Set the appearance of the calendar in the drop-down window
               dateEdit.Properties.CalendarView = DevExpress.XtraEditors.Repository.CalendarView.TouchUI;
           }
        //...
       }
   }
   ```

   ***
   [`CustomizeViewItemControl`]: xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[])
   [`Control`]: xref:DevExpress.ExpressApp.Editors.ViewItem.Control

3. Run the application and open the **Employee** Detail View. The **Birthday** editor shows a scrollable date picker in its drop-down window:

   ASP.NET Core Blazor

   :   ![|Scrollable date picker in ASP.NET Core Blazor](~/images/blazor-tutorial-scrollable-datepicker-blazor.png)

   Windows Forms

   :   ![Scrollable date picker in Windows Forms](~/images/blazor-tutorial-scrollable-datepicker-winforms.png)

> [!TIP]
> For general information on Property Editor architecture and UI Controls used by XAF, review the following articles: 
>  * [](xref:402189)
>  * [](xref:112679)
>  * [](xref:113014)

## Next Lesson

[](xref:402141)
