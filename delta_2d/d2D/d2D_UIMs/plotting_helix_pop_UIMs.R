library(tidyverse)
library(viridis)
df = read.table("/Users/Matteo/Dropbox (ELELAB)/UIMs_2019/data_to_share/analysis_NMRdata/dataframe_UIMs_NMR.txt", header = FALSE, fill = TRUE)
df <- tibble::rowid_to_column(df, "ID")
df = subset(df, select = -c(V1) )
colnames(df) <- c("ID", "AT3 UIM1","AT3 UIM1 helix pop.", "AT3 UIM2","AT3 UIM2 helix pop.", "AT3 UIM3","AT3 UIM3 helix pop.", "VPS27 UIM1","VPS27 UIM1 helix pop.",
                    "STAM1 UIM","STAM1 UIM helix pop.", "STAM2 UIM","STAM2 UIM helix pop.", "USP25 UIM1","USP25 UIM1 helix pop.", "USP25 UIM2","USP25 UIM2 helix pop.", "USP28 UIM","USP28 UIM helix pop.",
                    "RAP80 UIM1","RAP80 UIM1 helix pop.", "RAP80 UIM2","RAP80 UIM2 helix pop.")

df <- df %>% 
  gather(keys, values, c("AT3 UIM1 helix pop.","AT3 UIM2 helix pop.","AT3 UIM3 helix pop.","VPS27 UIM1 helix pop.","STAM1 UIM helix pop.","STAM2 UIM helix pop.","USP25 UIM1 helix pop.","USP25 UIM2 helix pop.", "USP28 UIM helix pop.", "RAP80 UIM1 helix pop.","RAP80 UIM2 helix pop."))

p <- ggplot(df, aes(ID, values)) +
     geom_col(aes(fill = keys)) +
     facet_wrap(~ keys) +
     scale_color_viridis() + theme_bw() + scale_fill_viridis(discrete=TRUE) + 
     theme(strip.placement = "outside",
        strip.text.y.left = element_text(angle = 0, vjust = 1),
        strip.background = element_blank(),
        strip.text.x = element_blank(),
        panel.spacing.y = unit(1.5, "lines"),
        panel.background = element_rect(fill = "white",
                                        color = NA)) +
     theme(axis.title.x=element_blank(),
           axis.text.x=element_blank(),
           axis.ticks.x=element_blank())
ggsave("d2D_helicity.UIMs.pdf",p, width=13, height=7, units="in", scale=0.7, dpi=600)





##############all#####################

library(tidyverse)
library(viridis)
df = read.table("/Users/Matteo/Dropbox (ELELAB)/UIMs_2019/data_to_share/analysis_NMRdata/dataframe_all_UIMs_NMR.txt", header = FALSE, fill = TRUE)
df <- tibble::rowid_to_column(df, "ID")
df = subset(df, select = -c(V1) )
colnames(df) <- c("ID", "AT3 UIM1 sbin","AT3 UIM1 sbin helix pop.", "AT3 UIM1 bmrb16405","AT3 UIM1 bmrb16405 helix pop.", "AT3 UIM1 bmrb27380","AT3 UIM1 bmrb27380 helix pop.", 
                  "AT3 UIM2 sbin","AT3 UIM2 sbin helix pop.", "AT3 UIM2 bmrb16405","AT3 UIM2 bmrb16405 helix pop.", "AT3 UIM2 bmrb27380","AT3 UIM2 bmrb27380 helix pop.", 
                  "AT3 UIM3","AT3 UIM3 Gary helix pop.", "AT3 UIM3 bmrb27380","AT3 UIM3 bmrb27380 helix pop.",
                  "VPS27 UIM1","VPS27 UIM1 helix pop.",
                  "STAM1 UIM","STAM1 UIM helix pop.", "STAM2 UIM","STAM2 UIM helix pop.", "USP25 UIM1","USP25 UIM1 helix pop.", "USP25 UIM2","USP25 UIM2 helix pop.", "USP28 UIM","USP28 UIM helix pop.",
                  "USP28 UIM sec","USP28 UIM sec helix pop.", "RAP80 UIM1","RAP80 UIM1 helix pop.", "RAP80 UIM2","RAP80 UIM2 helix pop.")

df <- df %>% 
  gather(keys, values, c("AT3 UIM1 sbin helix pop.", "AT3 UIM1 bmrb16405 helix pop.", "AT3 UIM1 bmrb27380 helix pop.", "AT3 UIM2 sbin helix pop.", "AT3 UIM2 bmrb16405 helix pop.", "AT3 UIM2 bmrb27380 helix pop.", "AT3 UIM3 Gary helix pop.", "AT3 UIM3 bmrb27380 helix pop.", "VPS27 UIM1 helix pop.","STAM1 UIM helix pop.","STAM2 UIM helix pop.","USP25 UIM1 helix pop.","USP25 UIM2 helix pop.", "USP28 UIM helix pop.", "USP28 UIM sec helix pop.", "RAP80 UIM1 helix pop.","RAP80 UIM2 helix pop."))

p <- ggplot(df, aes(ID, values)) +
  geom_col(aes(fill = keys)) +
  facet_wrap(~ keys) +
  scale_color_viridis() + theme_bw() + scale_fill_viridis(discrete=TRUE) + 
  theme(strip.placement = "outside",
        strip.text.y.left = element_text(angle = 0, vjust = 1),
        strip.background = element_blank(),
        strip.text.x = element_blank(),
        panel.spacing.y = unit(1.5, "lines"),
        panel.background = element_rect(fill = "white",
                                        color = NA)) +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank())
ggsave("d2D_helicity.alldataset.UIMs.pdf",p, width=13, height=7, units="in", scale=0.7, dpi=600)


############AT-3 UIMs#################

library(tidyverse)
library(viridis)
df = read.table("/Users/Matteo/Dropbox (ELELAB)/UIMs_2019/data_to_share/analysis_NMRdata/dataframe_AT3_UIMs_NMR.txt", header = FALSE, fill = TRUE)
df <- tibble::rowid_to_column(df, "ID")
df = subset(df, select = -c(V1) )
colnames(df) <- c("ID", "AT3 UIM1 sbin","AT3 UIM1 sbin helix pop.", "AT3 UIM1 bmrb16405","AT3 UIM1 bmrb16405 helix pop.", "AT3 UIM1 bmrb27380","AT3 UIM1 bmrb27380 helix pop.", "AT3 UIM2 sbin","AT3 UIM2 sbin helix pop.", "AT3 UIM2 bmrb16405","AT3 UIM2 bmrb16405 helix pop.", "AT3 UIM2 bmrb27380","AT3 UIM2 bmrb27380 helix pop.", "AT3 UIM3","AT3 UIM3 Gary helix pop.", "AT3 UIM3 bmrb27380","AT3 UIM3 bmrb27380 helix pop.")

df <- df %>% 
  gather(keys, values, c("AT3 UIM1 sbin helix pop.", "AT3 UIM1 bmrb16405 helix pop.", "AT3 UIM1 bmrb27380 helix pop.", "AT3 UIM2 sbin helix pop.", "AT3 UIM2 bmrb16405 helix pop.", "AT3 UIM2 bmrb27380 helix pop.", "AT3 UIM3 Gary helix pop.", "AT3 UIM3 bmrb27380 helix pop."))

p <- ggplot(df, aes(ID, values)) +
  geom_col(aes(fill = keys)) +
  facet_wrap(~ keys) +
  scale_color_viridis() + theme_bw() + scale_fill_viridis(discrete=TRUE) + 
  theme(strip.placement = "outside",
        strip.text.y.left = element_text(angle = 0, vjust = 1),
        strip.background = element_blank(),
        strip.text.x = element_blank(),
        panel.spacing.y = unit(1.5, "lines"),
        panel.background = element_rect(fill = "white",
                                        color = NA)) +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank())
ggsave("d2D_helicity.AT3.UIMs.pdf",p, width=13, height=7, units="in", scale=0.7, dpi=600)


