Name:           ros-melodic-rosmon
Version:        2.0.0
Release:        0%{?dist}
Summary:        ROS rosmon package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-rosmon-core
Requires:       ros-melodic-rqt-rosmon
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-rosmon-core
BuildRequires:  ros-melodic-rqt-rosmon

%description
Node launcher and monitor for ROS. rosmon is a replacement for the roslaunch
tool, focused on performance, remote monitoring, and usability.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Mar 11 2019 Max Schwarz <max.schwarz@uni-bonn.de> - 2.0.0-0
- Autogenerated by Bloom

* Mon Oct 29 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.10-0
- Autogenerated by Bloom

* Thu Sep 20 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.9-0
- Autogenerated by Bloom

* Tue Aug 07 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.8-0
- Autogenerated by Bloom

* Mon May 28 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.7-0
- Autogenerated by Bloom

* Thu May 24 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.4-0
- Autogenerated by Bloom

* Sat May 05 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.3-0
- Autogenerated by Bloom

* Fri Apr 13 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.1-0
- Autogenerated by Bloom

* Fri Apr 13 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.0-0
- Autogenerated by Bloom

