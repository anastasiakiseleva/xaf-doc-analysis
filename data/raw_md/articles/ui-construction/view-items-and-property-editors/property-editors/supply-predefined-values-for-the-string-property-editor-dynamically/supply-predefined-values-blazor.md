---
uid: "404597"
title: Supply Predefined Values for the String Property Editor Dynamically (ASP.NET Core Blazor)
---
# Supply Predefined Values for the String Property Editor Dynamically (ASP.NET Core Blazor)

This topic describes how to implement a custom Property Editor for an ASP.NET Core Blazor application and how to dynamically populate the editor's drop-down list with predefined values. In the scenario below, the editor is used to edit a business object's `CultureCode` (locale) property of the `String` type. The drop-down list of the Property Editor's control displays cultures returned by the @System.Globalization.CultureInfo.GetCultures* method.

> [!NOTE]
> You can also use the @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PredefinedValues property to specify predefined values in the [Model Editor](xref:112582). This approach is simpler as it requires no additional code, but in this case you cannot dynamically update the list of values in code.

To implement a Property Editor and supply predefined values for it, follow the steps below:

1. Add a new `CultureInfoPropertyEditor` class to your [ASP.NET Core Blazor Application Project](xref:118045). Inherit the newly created class from the `BlazorPropertyEditorBase` class and override the `CreateComponentModel` method to create a `DxComboBoxModel` object. This object defines the @DevExpress.Blazor.DxComboBox`2 component. 

    Apply the [PropertyEditor](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute) attribute to the editor. In the attribute declaration, indicate `String` as the corresponding property type.

    ```csharp
    using System.Globalization;
    using DevExpress.Blazor;
    using DevExpress.ExpressApp.Blazor.Components.Models;
    using DevExpress.ExpressApp.Blazor.Editors;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.ExpressApp.Model;

    namespace YourSolutionName.Blazor.Server.Controllers;

    [PropertyEditor(typeof(string), "CultureInfoPropertyEditor", false)]
    public class CultureInfoPropertyEditor : BlazorPropertyEditorBase {
        public CultureInfoPropertyEditor(Type objectType, IModelMemberViewItem model) : base(objectType, model) { }
        protected override IComponentModel CreateComponentModel() {
            DxComboBoxModel<string, string> componentModel = new DxComboBoxModel<string, string>();

            List<string> data = new List<string>();
            foreach(CultureInfo culture in CultureInfo.GetCultures(CultureTypes.AllCultures)) {
                data.Add($"{culture.EnglishName} ({culture.Name})");
            }

            componentModel.Data = data;
            componentModel.AllowUserInput = true;
            componentModel.FilteringMode = DataGridFilteringMode.Contains;
            componentModel.ClearButtonDisplayMode = AllowNull ? DataEditorClearButtonDisplayMode.Auto : DataEditorClearButtonDisplayMode.Never;
            componentModel.NullText = NullText;
            return componentModel;
        }
    }
    ```

2. Apply the [EditorAlias](xref:DevExpress.Persistent.Base.EditorAliasAttribute) attribute to the required property in the business class's definition. In this example, we use the implemented Property Editor for a business object's `CultureCode` property:

    ```csharp
    namespace YourSolutionName.Module.BusinessObjects;
    // ...  
    public class YourBusinessClass {
        //... 
        [EditorAlias("CultureInfoPropertyEditor")]
        public virtual String CultureCode { get; set; }
    }
    ```

    The `EditorAlias` attribute changes the `PropertyEditorType` property of the Application Model's @DevExpress.ExpressApp.Model.IModelMember node. This node corresponds to the `CultureCode` property. You can apply the same change in the [Model Editor](xref:112582). 

    You can also implement an @DevExpress.ExpressApp.Editors.IComplexViewItem in this Property Editor. This interface allows the editor to access the `XafApplication` instance and use an Object Space to load data from an application database.
    
3. Build and run your application. The image below shows the resulting Property Editor:

    ![DevExpress XAF for Blazor - String Property Editor with Predefined Values](~/images/supply-predefined-values-dynamically-blazor.png)
