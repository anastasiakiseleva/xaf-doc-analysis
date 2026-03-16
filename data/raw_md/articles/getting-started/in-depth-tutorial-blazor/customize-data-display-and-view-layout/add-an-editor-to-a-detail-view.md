---
uid: "403217"
title: Display a Nested Property Editor in a Detail View
owner: Anastasiya Kisialeva
---
# Display a Nested Property Editor in a Detail View

This lesson explains how to make the editor of a property visible in a [Detail View](xref:112611).

The instructions below show how to locate the **Department.Office** nested property and make it visible in the **Employee** Detail View.

> [!NOTE]
> Before you proceed, take a moment to review the previous lesson:
> * [Place an Action in a Different Location](xref:402145)

## Step-by-Step Instructions

1. Open the _Model.DesignedDiffs.xafml_ file in the [Model Editor](xref:112582).

2. Navigate to the **Views** | **MySolution.Module.BusinessObjects** | **Employee** node. Expand the **Employee_DetailView** child node and click the **Layout** node.

3. The Model Editor displays a design surface that imitates the **Employee** Detail View. Right-click the View's empty space and choose **Customize Layout** from the context menu:

   ![|Start layout customization|](~/images/blazor-tutorial-customize-layout-context-menu.png) 

4. In the invoked **Customization** window, click the **Add** button:
    
   ![|Customization Window|](~/images/blazor-tutorial-customization-window.png) 

5. In the **Object Model** dialog, expand the **Department** node, check the **Office** checkbox, and click **OK**.

   ![|Object Model Window|](~/images/blazor-tutorial-object-model-window.png) 

6. The **Office:** item appears on the **Hidden Items** tab of the **Customization** window:

   ![|A new field is added to the Object Model Window|](~/images/blazor-tutorial-customization-window-new-field.png) 

7. Drag the **Office:** item to the required position of the **Employee** Detail View.

   ![|Add Layout Item Department.Office|](~/images/blazor-tutorial-add-property-layout.gif)

8. Run the application, open the **Employee** Detail View, and find the **Office** editor:

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor: the new editor in the Detail View|](~/images/blazor-tutorial-add-property-editor-result-blazor.png)

   Windows Forms:

   :   ![Windows Forms: the new editor in the Detail View](~/images/blazor-tutorial-add-property-editor-result-winforms.png)

## Runtime Customization in ASP.NET Core Blazor

In an XAF ASP.NET Core Blazor application, you can also customize the Detail View layout at runtime. For more information, refer to the following topic: [](xref:404353).

1. Navigate to the **Employee** Detail View. Right-click the layout and select the **Customize Layout** option in the context menu.
2. In the invoked **Customization** form, click the **Customize** button under the **Hidden Items** list.
   
   ![ASP.NET Core Blazor: Hidden Items list in the Customization form, DevExpress](~/images/xaf-blazor-hidden-items-customization-devexpress.png)

3. In the invoked **Object Model** dialog window, expand the **Department** node, check the **Office** checkbox, and click **OK**.

   ![ASP.NET Core Blazor: Object Model dialog window, DevExpress](~/images/xaf-blazor-object-model-dialog-window-devexpress.png)

   > [!NOTE]
   > If you have an extensive and complicated data model, the structure in the **Object Model** dialog window may be confusing. To see the path to a reference property, hover your mouse over the property in the **Object Model** dialog window. This may help you distinguish between similar properties.

4. The **Office** item now appears in the **Hidden Items** list of the **Customization** window.

   ![ASP.NET Core Blazor: The Office item in the Hidden Items list, DevExpress](~/images/xaf-blazor-item-appears-in-hidden-items-list-devexpress.png)

5. Drag the **Office** item to the required position in the **Employee** Detail View.

>[!NOTE]
> To remove unnecessary hidden items, uncheck them in the **Object Model** dialog window.

## Next Lesson

[Change List View Filters](xref:403238)
