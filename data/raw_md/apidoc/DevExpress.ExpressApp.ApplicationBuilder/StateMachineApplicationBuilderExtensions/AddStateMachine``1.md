---
uid: DevExpress.ExpressApp.ApplicationBuilder.StateMachineApplicationBuilderExtensions.AddStateMachine``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.StateMachine.StateMachineOptions})
name: AddStateMachine<TBuilder>(IModuleBuilder<TBuilder>, Action<StateMachineOptions>)
type: Method
summary: '[!include[<\[State Machine Module\](xref:113713)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: |-
    public static IModuleBuilder<TBuilder> AddStateMachine<TBuilder>(this IModuleBuilder<TBuilder> builder, Action<StateMachineOptions> configureOptions = null)
        where TBuilder : IApplicationBuilder<TBuilder>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.StateMachine.StateMachineOptions}
    defaultValue: "null"
    description: Options that you can use to configure the State Machine Module.
  typeParameters:
  - id: TBuilder
    description: The @DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder or @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder type.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[AddStateMachine_example](~/templates/AddStateMachine_example.md)]