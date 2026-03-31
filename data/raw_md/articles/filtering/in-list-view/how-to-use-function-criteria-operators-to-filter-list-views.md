---
uid: "112809"
seealso: []
title: 'How to: Use Function Criteria Operators to Filter List Views'
---
# How to: Use Function Criteria Operators to Filter List Views

The **XAF** provides various approaches to filter List Views: [on data source level](xref:112988), [via the Application Model](xref:112990) and [on the UI specific level](xref:112652). In each of these approaches, you may need to set static variables as filter criteria values. For example, the filter "Task.DueDate must be set to the current date" needs the CurrentDate variable, calculated every time it is required. For this purpose, the use Function Criteria Operators. They represent functions you can use in criteria. In this topic, you will learn how to use these Function Criteria Operators when setting filter criteria for the Task List View. To see a full list of built-in Function Criteria Operators and learn how to implement custom ones, refer to the [Function Criteria Operators](xref:113307) topic.

Since the technique for using Function Criteria Operators is common to any filtering approach, both in code and the [Model Editor](xref:112582), the [](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute) will be chosen for demonstration.

> [!NOTE]
> Before reviewing the example, be sure to read the "Important Remark on the DateTime Function Criteria Operators" section of the [Function Criteria Operators](xref:113307) topic.

The following code demonstrates how to implement various filters using the **LocalDateTimeToday**, **LocalDateTimeLastWeek** and **LocalDateTimeThisWeek** Function Criteria Operators:

[!include[ListViewFilterAttribute_example](~/templates/ListViewFilterAttribute_example.md)]

The code above generates several Filter child nodes for the [Application Model](xref:112580)'s **Views** | **Task_ListView** node:

![FCO_ListViews](~/images/fco_listviews117059.png)
> [!NOTE]
> You could generate these nodes manually in the Model Editor.

The following image demonstrates the Filter Action that contains all the filters provided by the code above:

![Read-OnlyParameters for List Views_Result](~/images/read-onlyparameters-for-list-views_result115588.png)
