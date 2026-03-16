---
uid: "113287"
seealso:
- linkId: "112621"
- linkId: "113141"
- linkId: "113283"
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/t247610/winforms-data-grid-customize-data-aware-export-output
  altText: "How to: Customize the GridControl's Data-Aware Export Output"
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportable
title: 'How to: Customize the Export Action Behavior'
owner: Ekaterina Kiseleva
---
# How to: Customize the Export Action Behavior

## Export Action Availability

List Views can show the **Export** action if the List Editor implements the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface. When it does, the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) enables the **Export** action for that List View. This applies to the following editors:

- ASP.NET Core Blazor: Chart List, Tree List, Grid List.
- WinForms: Chart List, Pivot List, Scheduler List, Tree List, Grid List.

Each List Editor specifies [supported export formats](xref:DevExpress.ExpressApp.SystemModule.IExportable.SupportedExportFormats) (part of the [IExportable](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface). This format list populates the Export Action's [Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection - the sub-menu that allows you to select the file type.

## Customization Basics

To customize the Export Action's behavior, first access the Export Controller. Each platform uses its own controller class, derived from a common ancestor - [](xref:DevExpress.ExpressApp.SystemModule.ExportController). You may want to use platform-specific features, or implement cross-platform changes using the base class API.

See the list below for available platforms and Export Controller classes you may want to use:

- [](xref:DevExpress.ExpressApp.Win.SystemModule.WinExportController) (WinForms): Exports data to a file stream and invokes a Save File Dialog before the export operation.
- [](xref:DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController) (ASP.NET Core Blazor): Exports data to a memory stream. This export option is available only for property editors of the @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor type. Refer to the following topic for more information: [](xref:113683).
- [](xref:DevExpress.ExpressApp.SystemModule.ExportController) (base class): Use this class's API if you want to make changes across multiple platforms. 

Once you choose the appropriate controller type, you can assign a handler to one of the following events:

- [ExportController.CustomGetDefaultFileName](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomGetDefaultFileName) to change the file name.
- [ExportController.CustomExport](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomExport)/[BlazorExportController.CustomizeGridExport](xref:DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController.CustomizeGridExport) to customize export options or access and adjust the control before the export operation starts. 
- [ExportController.Exported](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exported)/[BlazorExportController.GridExported](xref:DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController.GridExported) to perform any required actions after the export is complete.


## Cross-Platform Code: Change the File Name

WinForms applications invoke the Save File Dialog before export. This dialog specifies the default file name that is generated from the caption of the List View used to export data. ASP.NET Core Blazor applications export data to a memory stream that can be saved as a file. The file's default name is generated the same way as in WinForms applications.

Subscribe to the [ExportController.CustomGetDefaultFileName](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomGetDefaultFileName) event to change the file name. The base [](xref:DevExpress.ExpressApp.SystemModule.ExportController) class contains this event. The following code accesses the **ExportController** object and handles its event:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
//...
public partial class CustomizeExportController : ViewController {
    public CustomizeExportController() {
        InitializeComponent();
        TargetViewType = ViewType.ListView;
    }
    private ExportController exportController;
    protected override void OnActivated() {
         base.OnActivated();
         exportController = Frame.GetController<ExportController>();
         if (exportController != null) {
             exportController.CustomGetDefaultFileName += exportController_CustomGetDefaultFileName;
         }
    }
    void exportController_CustomGetDefaultFileName(
        object sender, CustomGetDefaultFileNameEventArgs e) {
        // Set a custom file name
        e.FileName = e.FileName + "_" + DateTime.Now.ToString("MM.dd.yy");
    }
    protected override void OnDeactivated() {
         if (exportController != null) {
             exportController.CustomGetDefaultFileName -= exportController_CustomGetDefaultFileName;
         }
        base.OnDeactivated();
    }
}
```
***

The following image illustrates that the name specified in the **CustomGetDefaultFileName** event handler is used as the exported file's default name:

![CustomExport_FileName](~/images/customexport_filename117051.png)


## Shared Code for WinForms and ASP.NET Core Blazor: Export Option Customization Basics

To customize export options, subscribe to the [ExportController.CustomExport](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomExport) event and use the [ExportOptions](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportOptions) parameter. This parameter can return different [ExportOptionsBase](xref:DevExpress.XtraPrinting.ExportOptionsBase) descendants based on the platform and export format. The event's [CustomExportEventArgs.ExportTarget](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportTarget) parameter specifies the format the user chose. 

The code below reads the exported View's caption and assigns it to the sheet title in the exported XLS file:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
using DevExpress.XtraPrinting;
// ...
public partial class CustomizeExportController : ViewController {
    public CustomizeExportController() {
        InitializeComponent();
        TargetViewType = ViewType.ListView;
    }
    private ExportController exportController;
    protected override void OnActivated() {
        base.OnActivated();
        exportController = Frame.GetController<ExportController>();
        exportController.CustomExport += CustomExport;
    }
    protected virtual void CustomExport(object sender, CustomExportEventArgs e) {
        //Customize Export Options
        if (e.ExportTarget == ExportTarget.Xls) {
            XlsExportOptions options = e.ExportOptions as XlsExportOptions;
            if (options == null) {
               options = new XlsExportOptions();
            }
            options.SheetName = View.Caption;
            options.ShowGridLines = true;
            e.ExportOptions = options;
        }
    }
    protected override void OnDeactivated() {
        exportController.CustomExport -= new EventHandler<CustomExportEventArgs>(CustomExport);
        base.OnDeactivated();
    }
}
```
***

In the code above, the exported View's caption is used as the sheet's name in the exported XLS file.

![Export_6](~/images/export_6116765.png)

To customize export options in a platform-specific application only, access the corresponding controller:

ASP.NET Core Blazor
:   @DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController
Windows Forms
:   @DevExpress.ExpressApp.Win.SystemModule.WinExportController

These Controllers are [](xref:DevExpress.ExpressApp.SystemModule.ExportController) descendants, and they expose the **CustomExport** event as well.

When you customize export for certain List Editor types, you can cast the event's **ExportOptions** parameter to [](xref:DevExpress.XtraPrinting.XlsExportOptionsEx). This class offers a few additional settings compared to [](xref:DevExpress.XtraPrinting.XlsExportOptions).

## ASP.NET Core Blazor: Customize Export Options

### CSV, XLS, XLSX Export

In ASP.NET Core Blazor applications, subscribe to the [BlazorExportController.CustomizeGridExport](xref:DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController.CustomizeGridExport) event and use the event handler's [Options](xref:DevExpress.ExpressApp.Blazor.SystemModule.GridExportEventArgsBase`1.Options) parameter to access export options of the [](xref:DevExpress.XtraPrinting.ExportTarget). The options object type depends on the export format.

For example, when you export data to [Excel format](xref:DevExpress.XtraPrinting.ExportTarget.Xlsx), the **Options** parameter is a @DevExpress.Blazor.GridXlExportOptions object.

[!include[blazor-export-options](~/templates/blazor-export-options.md)]

### PDF Export

[!include[blazor-pdf-export-options](~/templates/blazor-pdf-export-options.md)]

## WinForms: Customize Export Options and Access the List Editor Control
This section describes customization of export options specific to a List Editor control type. The following code snippet changes settings for the WinForms Grid control. 

The example in this section adds user interaction to the export procedure. If a user exports data from a [GridListEditor](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) that contains collapsed groups, a message box appears that allows the user to choose whether to expand all groups.

The code handles the **CustomExport** event of the [](xref:DevExpress.ExpressApp.Win.SystemModule.WinExportController). The handler implements the following functionality:

- Accesses the underlying [](xref:DevExpress.XtraGrid.GridControl) and its GridView that displays data. 
- Iterates through group rows in the GridView and calls the [GridView.GetRowExpanded](xref:DevExpress.XtraGrid.Views.Grid.GridView.GetRowExpanded(System.Int32)) method to find collapsed rows.
- Shows a message box that allows a user to choose export behavior: expand all groups or keep row state as is.
- Sets the [GridView.OptionsPrint](xref:DevExpress.XtraGrid.Views.Grid.GridView.OptionsPrint) property according to the user's selection.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.XtraGrid.Views.Grid;
using DevExpress.ExpressApp.Win.SystemModule;
using DevExpress.ExpressApp.Win.Editors;
using DevExpress.ExpressApp.Win;
using System.Windows.Forms;
// ...
public partial class CustomizeExportControllerWin : ViewController {
     public CustomizeExportControllerWin() {
        InitializeComponent();
        TargetViewType = ViewType.ListView;
    }
    private WinExportController winExportController;
    protected override void OnActivated() {
        base.OnActivated();
        winExportController = Frame.GetController<WinExportController>();
        winExportController.CustomExport += winExportController_CustomExport;
    }
    void winExportController_CustomExport(object sender, CustomExportEventArgs e) {
        //Show a message before exporting a Grid List Editor
        GridListEditor gridListEditor = 
            ((DevExpress.ExpressApp.ListView)View).Editor as GridListEditor;
        if (gridListEditor != null) {
            GridView gridView = gridListEditor.GridView;
            if (HasCollapsedGroups(gridView)) {
                string message =
                   "There are collapsed groups in the grid. " +
                    "Expand all groups in the exported file?";
                gridView.OptionsPrint.ExpandAllGroups =
                   WinApplication.Messaging.GetUserChoice(message, GetMessageBoxCaption(),
                   MessageBoxButtons.YesNo)
                   == DialogResult.Yes;
            }
        }
    }
    private bool HasCollapsedGroups(GridView gridView) {
        if (gridView.GroupCount > 0) {
            int rowHandle = -1;
            while (gridView.IsValidRowHandle(rowHandle)) {
                if (!gridView.GetRowExpanded(rowHandle)) return true;
                rowHandle--;
            }
        }
        return false;
    }
    private string GetMessageBoxCaption() {
        return String.Format(
            "{0} {1}", winExportController.ExportAction.Caption,
                winExportController.ExportAction.SelectedItem);
    }
    protected override void OnDeactivated() {
        winExportController.CustomExport -= winExportController_CustomExport;
        base.OnDeactivated();
    }
}
```
***

The following message box is displayed when exporting a List View containing collapsed groups:

![Export_2](~/images/export_2116693.png)

> [!NOTE]
> Refer to the [How to: Localize Custom String Constants](xref:112655) topic to see how to make this message text localizable.

If the choice is "Yes", all grid rows will be exported.

![Export_4](~/images/export_4116695.png)

If the choice is "No", the rows belonging to the collapsed groups will not be included in the exported file.

![Export_3](~/images/export_3116694.png)

## Execute Custom Code After Export

### ASP.NET Core Blazor

You can notify users that a data export operation finished. Handle the [BlazorExportController.GridExported](xref:DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController.GridExported) event to do this:

[!include[blazor-after-export](~/templates/blazor-after-export.md)]

Refer to the following topic for an example of how to localize the message: [How to: Localize Custom String Constants](xref:112655).

### Windows Forms

After the export operation has finished, you can ask users whether the saved file should be opened. Handle the [ExportController.Exported](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exported) event to do this. The handler's [CustomExportEventArgs.Stream](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.Stream) parameter can be used to determine the exported file name.

# [C#](#tab/tabid-csharp)

```csharp
using System.IO;
using DevExpress.ExpressApp.Win;
using System.Windows.Forms;
using DevExpress.ExpressApp.Win.SystemModule;
//...
public partial class CustomizeExportControllerWin : ViewController {
    // ...
    private WinExportController winExportController;
    protected override void OnActivated() {
        base.OnActivated();
        // ...
        winExportController.Exported += 
            new EventHandler<CustomExportEventArgs>(winExportController_Exported);
    }
    void winExportController_Exported(object sender, 
            DevExpress.ExpressApp.SystemModule.CustomExportEventArgs e) {
        if (e.Stream is FileStream) {
            string fileName = ((FileStream)e.Stream).Name;
            if (File.Exists(fileName)) {
                e.Stream.Close();
                if (WinApplication.Messaging.GetUserChoice("Open the exported file?",
                        GetMessageBoxCaption(), MessageBoxButtons.YesNo) == DialogResult.Yes)
                    Process.Start(fileName);
            }
        }
    }
    protected override void OnDeactivated()  {
        winExportController.Exported -= 
            new EventHandler<CustomExportEventArgs>(winExportController_Exported);
        // ...
        base.OnDeactivated();
    }
}
```
***

The following image illustrates the message box shown after the export is finished:

![Export_5](~/images/export_5116696.png)

> [!NOTE]
> Refer to the [How to: Localize Custom String Constants](xref:112655) topic to see how to localize the message text.

If the user clicks "Yes", the exported file opens in an application associated with its type.

