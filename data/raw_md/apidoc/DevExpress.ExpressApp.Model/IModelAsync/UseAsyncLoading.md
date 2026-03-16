---
uid: DevExpress.ExpressApp.Model.IModelAsync.UseAsyncLoading
name: UseAsyncLoading
type: Property
summary: Specifies whether an XPO-based WinForms application loads a View's data asynchronously.
syntax:
  content: |-
    [DefaultValue(false)]
    [ModelBrowsable(typeof(UseAsyncLoadingVisibilityCalculator))]
    bool UseAsyncLoading { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true**, if an application loads a View's data asynchronously; otherwise, **false**."
seealso: []
---
You can specify this property for a List View, Detail View, or for all Views in your WinForms application. When this feature is active, the UI continues responding to user actions while data is being retrieved. For example, you can navigate to another View or close a current tab to cancel its View loading.

![Application with loading panel](~/images/UseAsyncLoading_Runtime.png)

Refer to the [Asynchronous Data Loading](xref:401747) topic for more information.
