import streamlit as st
import pandas as pd
from datetime import datetime

# 设置页面配置
st.set_page_config(
    page_title="数字游民签证助手",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 国家数据库
countries_db = {
    "葡萄牙": {
        "优势": ["欧盟身份", "税务优惠", "安全", "英语普及"],
        "劣势": ["生活成本较高", "语言障碍", "审批慢"],
        "收入要求": "每月€3040",
        "存款要求": "€9120",
        "每月生活费": "€800-1200",
        "税率": "10% (NHR计划)",
        "适合人群": ["高收入人群", "想拿欧盟身份", "重视安全"],
        "签证类型": "D7签证",
        "处理时间": "3-4个月",
        "匹配度": 0
    },
    "西班牙": {
        "优势": ["欧盟身份", "生活成本低", "气候好", "文化丰富"],
        "劣势": ["失业率较高", "语言障碍", "官僚复杂"],
        "收入要求": "每月€2151",
        "存款要求": "€25812",
        "每月生活费": "€600-900",
        "税率": "24% (前6年)",
        "适合人群": ["预算有限", "喜欢文化", "追求性价比"],
        "签证类型": "非盈利签证",
        "处理时间": "2-3个月",
        "匹配度": 0
    },
    "泰国": {
        "优势": ["生活成本极低", "美食丰富", "网络好", "华人多"],
        "劣势": ["非永久身份", "语言障碍", "气候炎热"],
        "收入要求": "每月$2000",
        "存款要求": "$10000",
        "每月生活费": "$300-500",
        "税率": "0% (境外收入免税)",
        "适合人群": ["预算极低", "喜欢热带", "吃辣爱好者"],
        "签证类型": "LTR签证",
        "处理时间": "1个月",
        "匹配度": 0
    },
    "墨西哥": {
        "优势": ["美国近", "生活成本低", "美食好", "文化丰富"],
        "劣势": ["安全问题", "语言障碍", "基础设施不稳定"],
        "收入要求": "每月$1500",
        "存款要求": "$2700",
        "每月生活费": "$400-600",
        "税率": "0% (境外收入免税)",
        "适合人群": ["想去美洲", "预算有限", "喜欢墨西哥菜"],
        "签证类型": "临时居民签证",
        "处理时间": "1-2个月",
        "匹配度": 0
    },
    "克罗地亚": {
        "优势": ["欧盟身份", "生活成本低", "海滩美", "英语普及"],
        "劣势": ["冬季寒冷", "经济不发达", "社交圈小"],
        "收入要求": "每月€2300",
        "存款要求": "€27600",
        "每月生活费": "€500-700",
        "税率": "12% (境外收入)",
        "适合人群": ["喜欢海滩", "预算有限", "想拿欧盟身份"],
        "签证类型": "数字游民签证",
        "处理时间": "1个月",
        "匹配度": 0
    }
}

def calculate_match(user_profile):
    """计算匹配度"""
    matches = []
    
    for country, data in countries_db.items():
        score = 50  # 基础分
        
        # 收入匹配
        monthly_income = user_profile.get("monthly_income", 0)
        if monthly_income >= 30000:  # 高收入
            if country in ["葡萄牙", "西班牙", "克罗地亚"]:
                score += 15
        elif monthly_income >= 15000:  # 中等收入
            if country in ["西班牙", "克罗地亚", "墨西哥"]:
                score += 15
        else:  # 低收入
            if country in ["泰国", "墨西哥"]:
                score += 15
        
        # 偏好匹配
        preference = user_profile.get("preference", "")
        if "海滩" in preference and country in ["泰国", "克罗地亚"]:
            score += 10
        if "城市" in preference and country in ["葡萄牙", "西班牙"]:
            score += 10
        if "低成本" in preference and country in ["泰国", "墨西哥", "克罗地亚"]:
            score += 10
        if "安全" in preference and country in ["葡萄牙", "克罗地亚"]:
            score += 10
        if "网络" in preference and country in ["泰国", "葡萄牙"]:
            score += 10
        
        # 家庭情况
        family = user_profile.get("family", "单身")
        if family == "单身":
            if country in ["泰国", "墨西哥", "克罗地亚"]:
                score += 5
        elif family == "情侣":
            if country in ["葡萄牙", "西班牙"]:
                score += 5
        
        # 职业匹配
        job = user_profile.get("job", "")
        if "程序员" in job or "设计师" in job:
            if country in ["泰国", "葡萄牙", "克罗地亚"]:
                score += 5
        
        data["匹配度"] = min(score, 100)
        matches.append((country, data))
    
    # 按匹配度排序
    matches.sort(key=lambda x: x[1]["匹配度"], reverse=True)
    return matches

def main():
    # 主界面
    st.title("🌍 数字游民签证助手")
    st.subheader("AI帮你找到最适合的数字游民目的地")
    
    # 创建两栏布局
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.header("📝 填写信息")
        
        # 用户输入表单
        with st.form("user_profile_form"):
            job = st.selectbox(
                "职业",
                ["程序员", "设计师", "自媒体", "咨询顾问", "其他"]
            )
            
            monthly_income = st.number_input(
                "月收入（人民币）",
                min_value=0,
                max_value=100000,
                value=20000,
                step=1000
            )
            
            continent = st.selectbox(
                "目标大洲",
                ["欧洲", "东南亚", "美洲"]
            )
            
            preference = st.multiselect(
                "偏好（可多选）",
                ["海滩", "城市", "低成本", "安全", "网络好"]
            )
            
            family = st.selectbox(
                "家庭情况",
                ["单身", "情侣", "带娃"]
            )
            
            submitted = st.form_submit_button("🚀 获取推荐", type="primary")
    
    with col2:
        if submitted:
            st.header("🎯 推荐结果")
            
            # 准备用户数据
            user_profile = {
                "job": job,
                "monthly_income": monthly_income,
                "continent": continent,
                "preference": ",".join(preference),
                "family": family
            }
            
            # 计算匹配度
            matches = calculate_match(user_profile)
            
            # 显示Top 3推荐
            for i, (country, data) in enumerate(matches[:3]):
                if i == 0:
                    st.success(f"### 🥇 第{i+1}推荐：{country}（匹配度：{data['匹配度']}%）")
                elif i == 1:
                    st.info(f"### 🥈 第{i+1}推荐：{country}（匹配度：{data['匹配度']}%）")
                else:
                    st.warning(f"### 🥉 第{i+1}推荐：{country}（匹配度：{data['匹配度']}%）")
                
                # 显示详细信息
                tab1, tab2, tab3 = st.tabs(["核心优势", "关键门槛", "成本预估"])
                
                with tab1:
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.markdown("**✅ 优势：**")
                        for adv in data["优势"]:
                            st.markdown(f"- {adv}")
                    with col_b:
                        st.markdown("**❌ 劣势：**")
                        for dis in data["劣势"]:
                            st.markdown(f"- {dis}")
                
                with tab2:
                    st.markdown(f"**签证类型：** {data['签证类型']}")
                    st.markdown(f"**收入要求：** {data['收入要求']}")
                    st.markdown(f"**存款要求：** {data['存款要求']}")
                    st.markdown(f"**处理时间：** {data['处理时间']}")
                
                with tab3:
                    st.markdown(f"**每月生活费：** {data['每月生活费']}")
                    st.markdown(f"**税率：** {data['税率']}")
                    
                    # 计算年度成本
                    monthly_cost = int(data['每月生活费'].replace('€', '').replace('$', '').split('-')[0])
                    annual_cost = monthly_cost * 12
                    st.markdown(f"**预估年成本：** €{annual_cost:,}")
                
                st.markdown("---")
            
            # 显示用户输入摘要
            with st.expander("📊 查看您的输入信息"):
                st.json(user_profile)
        
        else:
            st.info("👈 请在左侧填写信息，获取个性化推荐")
            
            # 显示示例
            st.markdown("### 📝 示例")
            st.markdown("**职业：** 程序员")
            st.markdown("**月收入：** 25000人民币")
            st.markdown("**目标大洲：** 欧洲")
            st.markdown("**偏好：** 安全、网络好")
            st.markdown("**家庭情况：** 单身")
    
    # 添加页脚
    st.markdown("---")
    st.markdown("🚀 MVP版本 | 数据更新于2026年 | 仅供参考，具体政策请以官方为准")

if __name__ == "__main__":
    main()
