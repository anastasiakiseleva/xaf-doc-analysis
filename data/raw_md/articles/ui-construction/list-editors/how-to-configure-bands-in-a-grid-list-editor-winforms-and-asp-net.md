---
uid: "113694"
seealso:
- linkId: "113695"
- linkId: "114637"
- linkId: "9873"
title: 'How to: Configure Bands in a Grid List Editor'
owner: Anastasiya Kisialeva
---
# How to: Configure Bands in a Grid List Editor

This topic describes how to group grid columns using [bands](xref:113695) in an XAF application.

> [!TIP]
> This topic describes a scenario based on the `DemoTask` List View from the `MainDemo.EF.Core` project that ships with XAF. You can find this demo in the following folder: _[!include[PathToMainDemo](~/templates/path-to-main-demo-ef-core.md)]_.

1. In the **MainDemo.Module** project, run the [Model Editor](xref:112582) for the _Model.DesignedDiffs.xamfl_ file. In the node tree, navigate to the **Views** | **MainDemo.Module.BusinessObjects** | **DemoTask** | **DemoTask_ListView** node.

2. Select the **BandsLayout** child node. Set the [Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property to `true`.
	
	![Bands_BandsLayout.Enable](~/images/bands_bandslayout.enable117588.png)

3. You can now expand the **BandsLayout** node to access its child nodes (grid columns). To add a band, right-click **BandsLayout** and choose **Add…** | **Band**.
	
	![Bands_AddBand](~/images/bands_addband117587.png)

4. Select the newly added node and set its `Id` to `TaskDetails`.
	
	![XAF, Specify Band Id in Model Editor, DevExpress](~/images/bands_setidtotaskdetails117591.png)
	
	> [!NOTE]
	> XAF generates the [IModelBand.Caption](xref:DevExpress.ExpressApp.Model.IModelBand.Caption) property value automatically based on the `Id` value. You can change the caption if necessary.

5. Select columns that you want to add to the **TaskDetails** band (hold the <kbd>CTRL</kbd> key and click the corresponding nodes). Drag the selected columns to the **TaskDetails** band node.
	
	![XAF, Add Columns to a Band in Model Editor, DevExpress](~/images/bands_dragtotaskdetails117590.png)

6. Add another band and name it **Schedule**. Move the remaining columns to the band. Your band structure should look like this:
	
	![XAF, Band Structure in Model Editor, DevExpress](~/images/bands_dragtoscheduleresult117589.png)
	
	> [!TIP]
	> You can add a band inside an existing band to create multi-level band hierarchy.

7. Run the application.

   ASP.NET Core Blazor Result	
   :   ![|XAF ASP.NET Core Blazor Bands Example, DevExpress](~/images/xaf-blazor-bands-result-devexpress.png)

   Windows Forms Result
   :   ![|XAF Windows Forms Bands Example, DevExpress](~/images/bands_win117593.png)
