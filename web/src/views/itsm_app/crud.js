import { request } from "@/api/service";
import { BUTTON_STATUS_NUMBER } from "@/config/button";
import { urlPrefix as bookPrefix } from "./api";


export const crudOptions = vm => {
    return {
        pageOptions: {
            compact: true
        },
        options: {
            tableType: "vxe-table",
            rowKey: true, // 必须设置，true or false
            rowId: "id",
            height: "100%", // 表格高度100%, 使用toolbar必须设置
            highlightCurrentRow: false
        },
        rowHandle: {
            width: 140,
            view: {
                thin: true,
                text: "",
                // disabled() {
                //     return !vm.hasPermissions("Retrieve")
                // }
            },
            edit: {
                thin: true,
                text: "",
                disabled() {
                    return !vm.hasPermissions("Update")
                }
            },
            remove: {
                thin: true,
                text: "",
                disabled() {
                    return !vm.hasPermissions("Delete")
                }
            }
        },
        indexRow: {
            // 或者直接传true,不显示title，不居中
            title: "序号",
            align: "center",
            width: 100
        },
        viewOptions: {
            componentType: "form"
        },
        formOptions: {
            defaultSpan: 24, // 默认的表单 span
            width: "35%"
        },
        columns: [{
            title: "ID",
            key: "id",
            show: false,
            disabled: true,
            width: 90,
            form: {
                disabled: true
            }
        },
        {
            title: "工单号",
            key: "Sn",
            sortable: true,
            treeNode: true,

            type: "input",
            form: {
                editDisabled: true,
                rules: [
                    // 表单校验规则
                    { required: true, message: "工单号称必填" }
                ],
                component: {
                    props: {
                        clearable: true
                    },
                    placeholder: "请输入工单号"
                },
                itemProps: {
                    class: { yxtInput: true }
                }
            }
        },
        {
            title: "主题",
            key: "Summary",
            sortable: true,
            type: "input",
            form: {
                editDisabled: true,
                rules: [
                    // 表单校验规则
                    { required: true, message: "主题必填" }
                ],
                component: {
                    props: {
                        clearable: true
                    },
                    placeholder: "主题"
                },
                itemProps: {
                    class: { yxtInput: true }
                }
            }
        },
        {
            title: "建单人",
            key: "Creator",
            sortable: true,
            search: {
                component: {
                    props: {
                        clearable: true
                    }
                }
            },

            type: "input",
            form: {
                editDisabled: true,
                rules: [
                    // 表单校验规则
                    { required: true, message: "建单人必填" }
                ],
                component: {
                    props: {
                        clearable: true
                    },
                    placeholder: "建单人"
                },
                itemProps: {
                    class: { yxtInput: true }
                }
            }
        },

        ].concat(vm.commonEndColumns())
    };
};